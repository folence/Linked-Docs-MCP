"""Hybrid search combining semantic and keyword search."""

from typing import List, Dict, Tuple
from schemas.document import DocumentChunk
from .vector_store import VectorStore
from .keyword_search import KeywordSearcher
from .embedder import Embedder


class HybridSearchEngine:
    """
    Combines semantic (FAISS) and keyword (BM25) search with weighted scoring.
    """
    
    def __init__(
        self,
        vector_store: VectorStore,
        keyword_searcher: KeywordSearcher,
        embedder: Embedder,
        semantic_weight: float = 0.7,
        keyword_weight: float = 0.3
    ):
        """
        Initialize the hybrid search engine.
        
        Args:
            vector_store: Vector store for semantic search
            keyword_searcher: BM25 keyword searcher
            embedder: Text embedder
            semantic_weight: Weight for semantic search scores (0-1)
            keyword_weight: Weight for keyword search scores (0-1)
        """
        self.vector_store = vector_store
        self.keyword_searcher = keyword_searcher
        self.embedder = embedder
        self.semantic_weight = semantic_weight
        self.keyword_weight = keyword_weight
        
        # Normalize weights
        total_weight = semantic_weight + keyword_weight
        if total_weight > 0:
            self.semantic_weight = semantic_weight / total_weight
            self.keyword_weight = keyword_weight / total_weight
    
    def search(self, query: str, top_k: int = 10, expand_results: bool = True) -> List[Tuple[DocumentChunk, float]]:
        """
        Perform hybrid search combining semantic and keyword methods.
        
        Args:
            query: Search query
            top_k: Number of results to return
            expand_results: If True, include multiple chunks from highly relevant documents
            
        Returns:
            List of (DocumentChunk, score) tuples sorted by combined score
        """
        # Get results from both search methods
        # Request more results than needed to ensure good coverage after merging
        retrieval_k = top_k * 10
        
        # Semantic search
        query_embedding = self.embedder.encode_query(query)
        semantic_results = self.vector_store.search(query_embedding, top_k=retrieval_k)
        
        # Keyword search
        keyword_results = self.keyword_searcher.search(query, top_k=retrieval_k)
        
        # Merge results with weighted scores
        merged_scores = self._merge_results(semantic_results, keyword_results)
        
        # Apply title/metadata boosting
        merged_scores = self._apply_metadata_boost(merged_scores, query)
        
        # Sort by combined score
        sorted_results = sorted(merged_scores.values(), key=lambda x: x[1], reverse=True)
        
        # Normalize scores to 0-1 range BEFORE expansion
        # This ensures expansion uses the final normalized scores for threshold checks
        sorted_results = self._normalize_scores(sorted_results)
        
        # If expand_results is True, include multiple chunks from top documents
        # Now using normalized scores for threshold checks
        if expand_results:
            sorted_results = self._expand_top_documents(sorted_results, top_k)
        
        # Return expanded results - don't trim! 
        # The whole point of expansion is to return MORE context from top documents
        return sorted_results
    
    def _merge_results(
        self,
        semantic_results: List[Tuple[DocumentChunk, float]],
        keyword_results: List[Tuple[DocumentChunk, float]]
    ) -> Dict[str, Tuple[DocumentChunk, float]]:
        """
        Merge and weight results from both search methods.
        
        Args:
            semantic_results: Results from semantic search
            keyword_results: Results from keyword search
            
        Returns:
            Dictionary mapping chunk_id to (chunk, combined_score)
        """
        merged = {}
        
        # Add semantic results
        for chunk, score in semantic_results:
            weighted_score = score * self.semantic_weight
            merged[chunk.chunk_id] = (chunk, weighted_score)
        
        # Add/update with keyword results
        for chunk, score in keyword_results:
            weighted_score = score * self.keyword_weight
            
            if chunk.chunk_id in merged:
                # Combine scores if chunk appears in both
                existing_chunk, existing_score = merged[chunk.chunk_id]
                merged[chunk.chunk_id] = (existing_chunk, existing_score + weighted_score)
            else:
                merged[chunk.chunk_id] = (chunk, weighted_score)
        
        return merged
    
    def _apply_metadata_boost(
        self,
        merged_scores: Dict[str, Tuple[DocumentChunk, float]],
        query: str
    ) -> Dict[str, Tuple[DocumentChunk, float]]:
        """
        Boost scores based on title and metadata matches.
        
        Args:
            merged_scores: Initial merged scores
            query: Original query
            
        Returns:
            Updated scores with metadata boosts applied
        """
        query_lower = query.lower()
        query_words = set(query_lower.split())
        
        boosted = {}
        for chunk_id, (chunk, score) in merged_scores.items():
            boost_multiplier = 1.0
            
            # Title matching boost
            title = chunk.metadata.get("title", "").lower()
            if title:
                title_words = set(title.split())
                
                # Exact title match - huge boost
                if query_lower in title or title in query_lower:
                    boost_multiplier *= 3.0
                
                # Word overlap boost
                word_overlap = len(query_words & title_words)
                if word_overlap > 0:
                    # Boost proportional to overlap (up to 2x)
                    overlap_ratio = word_overlap / max(len(query_words), 1)
                    boost_multiplier *= (1.0 + overlap_ratio)
            
            # Apply boost
            boosted_score = score * boost_multiplier
            boosted[chunk_id] = (chunk, boosted_score)
        
        return boosted
    
    def _expand_top_documents(
        self,
        sorted_results: List[Tuple[DocumentChunk, float]],
        top_k: int
    ) -> List[Tuple[DocumentChunk, float]]:
        """
        Expand results by including multiple chunks from high-scoring documents.
        
        ANY document with max normalized score >= 0.7 will be expanded.
        This ensures all highly relevant documents get multi-chunk context.
        Scores are normalized before expansion, so the 0.7 threshold matches the
        final displayed scores users see.
        
        The number of chunks per document depends on its score:
        - Score ≥ 0.9: Include ALL chunks (complete document - perfect match)
        - Score ≥ 0.7: Include up to 6 chunks (comprehensive context)
        - Score ≥ 0.5: Include up to 4 chunks (substantial context)
        - Score ≥ 0.3: Include up to 2 chunks (key sections)
        - Score < 0.3: Include only the best matching chunk
        
        Total results are capped at top_k * 3 (e.g., 30 results for top_k=10).
        
        This ensures perfect matches return the entire document while keeping
        overall results manageable.
        
        Args:
            sorted_results: Results sorted by score
            top_k: Target number of results (used for calculating max total)
            
        Returns:
            Expanded list of results with additional chunks from high-scoring documents
        """
        if not sorted_results:
            return sorted_results
        
        # Group chunks by document
        doc_groups = {}
        for chunk, score in sorted_results:
            doc_id = chunk.document_id
            if doc_id not in doc_groups:
                doc_groups[doc_id] = []
            doc_groups[doc_id].append((chunk, score))
        
        # Build expanded results
        expanded = []
        seen_chunks = set()
        
        # First, add the top chunk from each top document
        for chunk, score in sorted_results[:top_k]:
            if chunk.chunk_id not in seen_chunks:
                expanded.append((chunk, score))
                seen_chunks.add(chunk.chunk_id)
        
        # Then, add more chunks from high-scoring documents
            # IMPORTANT: Only expand the TOP 5 documents to avoid returning too many results
        # Sort documents by their best score
        doc_max_scores = [(doc_id, max(score for _, score in chunks)) 
                          for doc_id, chunks in doc_groups.items()]
        doc_max_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Expand the top 5 documents with a max normalized score >= 0.7
        # We use the MAX normalized score across all chunks for each document
        # Scores are normalized (0-1 range) so the threshold directly matches displayed scores
        docs_to_expand = set([doc_id for doc_id, score in doc_max_scores[:5] if score >= 0.7])
        
        for doc_id, chunks_scores in doc_groups.items():
            # Skip if below score threshold
            if doc_id not in docs_to_expand:
                continue
            # Check if this document has a high-scoring chunk
            max_score = max(score for _, score in chunks_scores)
            
            # Determine how many chunks to include based on score
            # Perfect/near-perfect scores → ALL chunks (complete document)
            # Very high scores (≥0.7) → up to 6 chunks (comprehensive context)
            # High scores (≥0.5) → up to 4 chunks (substantial context)
            # Medium scores (≥0.3) → up to 2 chunks (key sections)
            # Lower scores → just the best chunk (already added above)
            if max_score >= 0.9:
                max_chunks = 999  # Perfect match - read the ENTIRE document
            elif max_score >= 0.7:
                max_chunks = 6  # Very relevant - read most of it
            elif max_score >= 0.5:
                max_chunks = 4  # Highly relevant - read key sections
            elif max_score >= 0.3:
                max_chunks = 2  # Relevant - read a couple sections
            else:
                max_chunks = 1  # Less relevant - just the best chunk
            
            if max_chunks > 1:
                # Fetch ALL chunks from this document from the vector store
                # This is KEY: we're not limited to chunks found by the search!
                all_doc_chunks = [
                    chunk for chunk in self.vector_store.chunks
                    if chunk.document_id == doc_id
                ]
                
                # Sort by chunk index for sequential reading
                all_doc_chunks.sort(key=lambda c: c.chunk_index)
                
                # Add chunks with their scores (use max_score for missing chunks)
                added_count = 0
                for chunk in all_doc_chunks:
                    if chunk.chunk_id not in seen_chunks and added_count < max_chunks:
                        # Use the existing score if we have it, otherwise use a derived score
                        chunk_score = max_score * 0.9  # Slightly lower than top chunk
                        for existing_chunk, existing_score in chunks_scores:
                            if existing_chunk.chunk_id == chunk.chunk_id:
                                chunk_score = existing_score
                                break
                        
                        expanded.append((chunk, chunk_score))
                        seen_chunks.add(chunk.chunk_id)
                        added_count += 1
        
        # Sort final results by score
        expanded.sort(key=lambda x: x[1], reverse=True)
        
        # Cap total results at a reasonable limit to avoid overwhelming output
        # This allows complete documents for top matches while keeping results manageable
        max_total_results = top_k * 3  # e.g., top_k=10 → max 30 results
        if len(expanded) > max_total_results:
            expanded = expanded[:max_total_results]
        
        return expanded
    
    def _normalize_scores(
        self,
        results: List[Tuple[DocumentChunk, float]]
    ) -> List[Tuple[DocumentChunk, float]]:
        """
        Normalize scores to 0-1 range.
        
        This is crucial after title boosting which can push scores > 1.
        
        Args:
            results: List of (chunk, score) tuples
            
        Returns:
            Same list with scores normalized to 0-1
        """
        if not results:
            return results
        
        # Find min and max scores
        scores = [score for _, score in results]
        min_score = min(scores)
        max_score = max(scores)
        
        # If all scores are the same, return as-is
        if max_score == min_score:
            return [(chunk, 1.0) for chunk, _ in results]
        
        # Normalize to 0-1 range
        normalized = []
        for chunk, score in results:
            normalized_score = (score - min_score) / (max_score - min_score)
            normalized.append((chunk, normalized_score))
        
        return normalized
    
    def get_stats(self) -> dict:
        """
        Get statistics about the search engine.
        
        Returns:
            Dictionary containing stats from both search methods
        """
        return {
            "vector_store": self.vector_store.get_stats(),
            "keyword_searcher": self.keyword_searcher.get_stats(),
            "semantic_weight": self.semantic_weight,
            "keyword_weight": self.keyword_weight,
        }


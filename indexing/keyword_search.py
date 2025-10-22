"""BM25-based keyword search."""

from typing import List, Tuple
from rank_bm25 import BM25Okapi
import numpy as np

from schemas.document import DocumentChunk


class KeywordSearcher:
    """
    Keyword-based search using BM25 algorithm.
    """
    
    def __init__(self):
        """Initialize the keyword searcher."""
        self.bm25 = None
        self.chunks = []
        self.tokenized_corpus = []
    
    def index_chunks(self, chunks: List[DocumentChunk]):
        """
        Index chunks for keyword search.
        
        This method REPLACES the existing index with the provided chunks.
        To rebuild the index with all chunks, pass vector_store.chunks.
        
        Args:
            chunks: List of DocumentChunk objects to index
        """
        if not chunks:
            return
        
        # Replace existing chunks (not extend) to avoid duplicates
        self.chunks = list(chunks)
        
        # Tokenize all chunk texts
        self.tokenized_corpus = [self._tokenize(chunk.text) for chunk in chunks]
        
        # Rebuild BM25 index with all chunks
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        
        print(f"Indexed {len(chunks)} chunks for keyword search. Total: {len(self.chunks)}")
    
    def search(self, query: str, top_k: int = 10) -> List[Tuple[DocumentChunk, float]]:
        """
        Search for chunks matching the query keywords.
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of (DocumentChunk, score) tuples
        """
        if not self.bm25 or len(self.chunks) == 0:
            return []
        
        # Tokenize query
        tokenized_query = self._tokenize(query)
        
        # Get BM25 scores
        scores = self.bm25.get_scores(tokenized_query)
        
        # Normalize scores to 0-1 range
        if len(scores) > 0 and scores.max() > 0:
            normalized_scores = scores / scores.max()
        else:
            normalized_scores = scores
        
        # Get top-k results
        top_indices = np.argsort(scores)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if idx < len(self.chunks):
                results.append((self.chunks[idx], float(normalized_scores[idx])))
        
        return results
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into words.
        
        Args:
            text: Text to tokenize
            
        Returns:
            List of tokens (lowercase words)
        """
        import re
        
        # Simple tokenization: lowercase, split on non-alphanumeric
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)
        return tokens
    
    def clear(self):
        """Clear all indexed data."""
        self.bm25 = None
        self.chunks = []
        self.tokenized_corpus = []
        print("Cleared keyword search index")
    
    def get_stats(self) -> dict:
        """
        Get statistics about the keyword index.
        
        Returns:
            Dictionary containing stats
        """
        return {
            "total_chunks": len(self.chunks),
            "avg_tokens_per_chunk": np.mean([len(tokens) for tokens in self.tokenized_corpus]) if self.tokenized_corpus else 0,
        }


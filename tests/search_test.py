#!/usr/bin/env python3
"""
Utility for testing and optimizing search results.

Usage:
    python search_test.py "your search query"
    python search_test.py "your search query" --top-k 20
    python search_test.py "your search query" --filter "Fuel"
    python search_test.py "your search query" --no-expand
    python search_test.py "your search query" --verbose
"""

import asyncio
import argparse
from collections import defaultdict
from indexing import Embedder, VectorStore, KeywordSearcher
from indexing.hybrid_search import HybridSearchEngine
from schemas.config import settings


def format_preview(text: str, max_length: int = 100) -> str:
    """Format text preview with ellipsis if too long."""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


async def main():
    parser = argparse.ArgumentParser(
        description="Search documentation and analyze results",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python search_test.py "fuel efficiency"
  python search_test.py "fuel types" --top-k 15 --verbose
  python search_test.py "modules" --filter "Efficiency" --no-expand
        """
    )
    
    parser.add_argument(
        "query",
        type=str,
        help="Search query"
    )
    
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Number of results to return (default: 10)"
    )
    
    parser.add_argument(
        "--filter",
        type=str,
        default=None,
        help="Filter results by document title (case-insensitive substring match)"
    )
    
    parser.add_argument(
        "--no-expand",
        action="store_true",
        help="Disable document expansion (only return initial search results)"
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed chunk content previews"
    )
    
    parser.add_argument(
        "--stats-only",
        action="store_true",
        help="Only show statistics, not individual chunks"
    )
    
    args = parser.parse_args()
    
    # Initialize search engine
    print("Initializing search engine...")
    print(f"  Embedding model: {settings.embedding_model}")
    print(f"  Chunk size: {settings.chunk_size}")
    print(f"  Chunk overlap: {settings.chunk_overlap}")
    print()
    
    embedder = Embedder(
        model_name=settings.embedding_model,
        device=settings.embedding_device
    )
    
    vector_store = VectorStore(
        embedding_dim=embedder.get_embedding_dimension(),
        store_path=settings.vector_store_path
    )
    vector_store.load()
    
    keyword_searcher = KeywordSearcher()
    keyword_searcher.index_chunks(vector_store.chunks)
    
    hybrid_search = HybridSearchEngine(
        embedder=embedder,
        vector_store=vector_store,
        keyword_searcher=keyword_searcher
    )
    
    # Perform search
    print(f"Searching for: '{args.query}'")
    print(f"  Top-k: {args.top_k}")
    print(f"  Expansion: {'disabled' if args.no_expand else 'enabled'}")
    if args.filter:
        print(f"  Filter: '{args.filter}'")
    print("=" * 80)
    print()
    
    results = hybrid_search.search(
        args.query,
        top_k=args.top_k,
        expand_results=not args.no_expand
    )
    
    # Apply filter if specified
    if args.filter:
        filter_lower = args.filter.lower()
        results = [
            (chunk, score) for chunk, score in results
            if filter_lower in chunk.metadata.get("title", "").lower()
        ]
    
    # Group results by document
    doc_results = defaultdict(list)
    for chunk, score in results:
        doc_id = chunk.document_id
        title = chunk.metadata.get("title", "Untitled")
        doc_results[doc_id].append({
            "title": title,
            "chunk": chunk,
            "score": score
        })
    
    # Calculate statistics
    total_chunks = len(results)
    total_docs = len(doc_results)
    
    print(f"RESULTS SUMMARY")
    print(f"  Total chunks: {total_chunks}")
    print(f"  From {total_docs} documents")
    print()
    
    if args.stats_only:
        # Just show document-level stats
        print(f"DOCUMENTS (sorted by best score):")
        print()
        
        # Sort documents by their best score
        doc_list = []
        for doc_id, chunks_data in doc_results.items():
            best_score = max(item["score"] for item in chunks_data)
            doc_list.append({
                "doc_id": doc_id,
                "title": chunks_data[0]["title"],
                "num_chunks": len(chunks_data),
                "best_score": best_score,
                "avg_score": sum(item["score"] for item in chunks_data) / len(chunks_data)
            })
        
        doc_list.sort(key=lambda x: x["best_score"], reverse=True)
        
        for i, doc_info in enumerate(doc_list, 1):
            print(f"{i}. {doc_info['title']}")
            print(f"   Chunks: {doc_info['num_chunks']}")
            print(f"   Best score: {doc_info['best_score']:.3f}")
            print(f"   Avg score:  {doc_info['avg_score']:.3f}")
            print()
    else:
        # Show detailed results
        print(f"DETAILED RESULTS:")
        print()
        
        # Sort documents by best score
        sorted_docs = sorted(
            doc_results.items(),
            key=lambda x: max(item["score"] for item in x[1]),
            reverse=True
        )
        
        for doc_num, (doc_id, chunks_data) in enumerate(sorted_docs, 1):
            title = chunks_data[0]["title"]
            num_chunks = len(chunks_data)
            best_score = max(item["score"] for item in chunks_data)
            
            print(f"## {doc_num}. {title}")
            print(f"   Document ID: {doc_id[:30]}...")
            print(f"   Chunks: {num_chunks} | Best score: {best_score:.3f}")
            print()
            
            # Sort chunks by index for sequential reading
            chunks_data.sort(key=lambda x: x["chunk"].chunk_index)
            
            for chunk_data in chunks_data:
                chunk = chunk_data["chunk"]
                score = chunk_data["score"]
                
                print(f"   Chunk {chunk.chunk_index} - Score: {score:.3f} - Length: {len(chunk.text)} chars")
                
                if args.verbose:
                    # Show first and last parts of chunk
                    preview_len = 150
                    if len(chunk.text) > preview_len * 2:
                        print(f"      Start: {format_preview(chunk.text[:preview_len], preview_len)}")
                        print(f"      ...({len(chunk.text) - preview_len*2} chars)...")
                        print(f"      End:   {format_preview(chunk.text[-preview_len:], preview_len)}")
                    else:
                        print(f"      {format_preview(chunk.text, preview_len)}")
                else:
                    print(f"      {format_preview(chunk.text, 80)}")
                
                print()
            
            print("-" * 80)
            print()
    
    # Expansion analysis (if enabled)
    if not args.no_expand and total_docs > 0:
        print(f"EXPANSION ANALYSIS:")
        
        # Count how many documents have multiple chunks
        multi_chunk_docs = sum(1 for chunks in doc_results.values() if len(chunks) > 1)
        avg_chunks_per_doc = total_chunks / total_docs
        
        print(f"  Documents with multiple chunks: {multi_chunk_docs}/{total_docs}")
        print(f"  Average chunks per document: {avg_chunks_per_doc:.1f}")
        print()
        
        # Show which documents were expanded
        expanded_docs = [(title, len(chunks)) 
                         for doc_id, chunks in doc_results.items()
                         for title in [chunks[0]["title"]]
                         if len(chunks) > 1]
        
        if expanded_docs:
            expanded_docs.sort(key=lambda x: x[1], reverse=True)
            print(f"  Expanded documents:")
            for title, count in expanded_docs:
                print(f"    - {title}: {count} chunks")
        print()
    
    # Score distribution
    print(f"SCORE DISTRIBUTION:")
    scores = [score for _, score in results]
    if scores:
        print(f"  Highest: {max(scores):.3f}")
        print(f"  Lowest:  {min(scores):.3f}")
        print(f"  Average: {sum(scores)/len(scores):.3f}")
        
        # Histogram
        score_ranges = [
            ("1.000", sum(1 for s in scores if s >= 0.95)),
            ("0.9-0.95", sum(1 for s in scores if 0.9 <= s < 0.95)),
            ("0.7-0.9", sum(1 for s in scores if 0.7 <= s < 0.9)),
            ("0.5-0.7", sum(1 for s in scores if 0.5 <= s < 0.7)),
            ("0.3-0.5", sum(1 for s in scores if 0.3 <= s < 0.5)),
            ("< 0.3", sum(1 for s in scores if s < 0.3)),
        ]
        
        print()
        print("  Score ranges:")
        for range_name, count in score_ranges:
            if count > 0:
                bar = "#" * min(count, 50)
                print(f"    {range_name:>10}: {bar} ({count})")


if __name__ == "__main__":
    asyncio.run(main())


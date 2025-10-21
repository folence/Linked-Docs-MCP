"""FAISS-based vector store for semantic search."""

from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np
import pickle
import faiss

from schemas.document import DocumentChunk


class VectorStore:
    """
    Vector storage and retrieval using FAISS.
    """
    
    def __init__(self, embedding_dim: int, store_path: Optional[Path] = None):
        """
        Initialize the vector store.
        
        Args:
            embedding_dim: Dimension of embedding vectors
            store_path: Path to save/load the index
        """
        self.embedding_dim = embedding_dim
        self.store_path = store_path
        self.index = None
        self.chunks = []  # Store chunk metadata
        self._initialize_index()
    
    def _initialize_index(self):
        """Initialize or load the FAISS index."""
        if self.store_path and self.store_path.exists():
            try:
                self.load()
            except Exception as e:
                print(f"Warning: Could not load existing index: {e}")
                print(f"Creating new FAISS index...")
                self.index = faiss.IndexFlatL2(self.embedding_dim)
        
        # Ensure index is created if load failed or path doesn't exist
        if self.index is None:
            # Create a new index using L2 distance
            # Using IndexFlatL2 for exact search (good for prototypes)
            # For production, could use IndexIVFFlat or IndexHNSW for faster approximate search
            self.index = faiss.IndexFlatL2(self.embedding_dim)
            print(f"Created new FAISS index with dimension {self.embedding_dim}")
    
    def add_chunks(self, chunks: List[DocumentChunk], embeddings: np.ndarray):
        """
        Add chunks and their embeddings to the index.
        
        Args:
            chunks: List of DocumentChunk objects
            embeddings: Numpy array of embeddings (shape: num_chunks x embedding_dim)
        """
        if len(chunks) != len(embeddings):
            raise ValueError("Number of chunks must match number of embeddings")
        
        if len(chunks) == 0:
            return
        
        # Ensure embeddings are float32 (required by FAISS)
        embeddings = embeddings.astype('float32')
        
        # Add to FAISS index
        self.index.add(embeddings)
        
        # Store chunk metadata
        self.chunks.extend(chunks)
        
        print(f"Added {len(chunks)} chunks to vector store. Total: {len(self.chunks)}")
    
    def search(self, query_embedding: np.ndarray, top_k: int = 10) -> List[Tuple[DocumentChunk, float]]:
        """
        Search for similar chunks using vector similarity.
        
        Args:
            query_embedding: Query embedding vector
            top_k: Number of results to return
            
        Returns:
            List of (DocumentChunk, distance) tuples
        """
        if self.index.ntotal == 0:
            return []
        
        # Ensure query is 2D array and float32
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)
        query_embedding = query_embedding.astype('float32')
        
        # Search
        top_k = min(top_k, self.index.ntotal)
        distances, indices = self.index.search(query_embedding, top_k)
        
        # Convert distances to similarity scores (inverse of L2 distance)
        # Normalize to 0-1 range
        distances = distances[0]  # Get first row
        indices = indices[0]
        
        # Convert L2 distances to similarity scores
        # Using negative exponential: similarity = exp(-distance)
        # This gives scores closer to 1 for similar items
        similarities = np.exp(-distances / 10.0)  # Scale factor of 10 for better distribution
        
        # Normalize to 0-1 range
        if len(similarities) > 0:
            min_sim = similarities.min()
            max_sim = similarities.max()
            if max_sim > min_sim:
                similarities = (similarities - min_sim) / (max_sim - min_sim)
        
        results = []
        for idx, score in zip(indices, similarities):
            if idx < len(self.chunks):
                results.append((self.chunks[idx], float(score)))
        
        return results
    
    def save(self):
        """Save the index and chunk metadata to disk."""
        if not self.store_path:
            print("No store path specified, skipping save")
            return
        
        # Create directory if it doesn't exist
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save FAISS index
        index_file = self.store_path / "faiss.index"
        faiss.write_index(self.index, str(index_file))
        
        # Save chunk metadata
        chunks_file = self.store_path / "chunks.pkl"
        with open(chunks_file, 'wb') as f:
            pickle.dump(self.chunks, f)
        
        print(f"Saved vector store to {self.store_path}")
    
    def load(self):
        """Load the index and chunk metadata from disk."""
        if not self.store_path or not self.store_path.exists():
            print("Store path does not exist, cannot load")
            return
        
        try:
            # Load FAISS index
            index_file = self.store_path / "faiss.index"
            if index_file.exists():
                self.index = faiss.read_index(str(index_file))
                print(f"Loaded FAISS index with {self.index.ntotal} vectors")
            else:
                print("No existing FAISS index found")
            
            # Load chunk metadata
            chunks_file = self.store_path / "chunks.pkl"
            if chunks_file.exists():
                with open(chunks_file, 'rb') as f:
                    self.chunks = pickle.load(f)
                print(f"Loaded {len(self.chunks)} chunk metadata entries")
            else:
                print("No existing chunk metadata found")
        
        except Exception as e:
            print(f"Error loading vector store: {e}")
            # Don't call _initialize_index here to avoid recursion
            raise
    
    def clear(self):
        """Clear all data from the index."""
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.chunks = []
        print("Cleared vector store")
    
    def get_stats(self) -> dict:
        """
        Get statistics about the vector store.
        
        Returns:
            Dictionary containing stats
        """
        return {
            "total_vectors": self.index.ntotal if self.index else 0,
            "total_chunks": len(self.chunks),
            "embedding_dim": self.embedding_dim,
        }


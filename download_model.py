import os

cache_dir = os.path.join(os.getcwd(), 'model_cache')
os.makedirs(cache_dir, exist_ok=True)

os.environ['SENTENCE_TRANSFORMERS_HOME'] = cache_dir
os.environ['HF_HOME'] = cache_dir

from sentence_transformers import SentenceTransformer

print("Downloading embedding model to local folder...")
print(f"Cache directory: {cache_dir}")

try:
    model = SentenceTransformer(
        'sentence-transformers/all-MiniLM-L6-v2',
        cache_folder=cache_dir
    )
    print("Model downloaded successfully!")
    print(f"Model location: {cache_dir}")

    test_embedding = model.encode("test sentence")
    print(f"Model working! Embedding dimension: {len(test_embedding)}")
    
except Exception as e:
    print(f"Error: {e}")
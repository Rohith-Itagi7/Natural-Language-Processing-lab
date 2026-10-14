
import re
from gensim.models import Word2Vec

# Step 1: Create a text corpus
sentences = [
    "machine learning is interesting",
    "deep learning uses neural networks",
    "machine learning uses algorithms",
    "neural networks learn from data",
    "deep learning is a part of machine learning",
    "python is useful for machine learning",
    "neural networks are used in deep learning",
    "algorithms learn patterns from data",
    "python supports data science",
    "machine learning models learn patterns"
]

# Step 2: Preprocess the sentences
processed_sentences = []

for sentence in sentences:
    sentence = sentence.lower()
    sentence = re.sub(r"[^a-z\s]", "", sentence)
    words = sentence.split()
    processed_sentences.append(words)

# Step 3: Train a Skip-Gram model
model = Word2Vec(
    sentences=processed_sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1,
    sg=1,
    seed=42,
    epochs=100
)

# Step 4: Display the vocabulary
print("Vocabulary:")
print(model.wv.index_to_key)

# Step 5: Display the embedding for a target word
target_word = "learning"

print(f"\nEmbedding for '{target_word}':")
print(model.wv[target_word])

print("\nEmbedding dimensions:")
print(len(model.wv[target_word]))

# Step 6: Find words with similar embeddings
print(f"\nWords similar to '{target_word}':")

for word, similarity in model.wv.most_similar(
    target_word, topn=5
):
    print(f"{word}: {similarity:.4f}")

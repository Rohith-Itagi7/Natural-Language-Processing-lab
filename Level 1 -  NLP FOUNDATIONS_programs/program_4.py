
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

# Step 3: Train a CBOW model
model = Word2Vec(
    sentences=processed_sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1,
    sg=0,
    seed=42,
    epochs=100
)

# Step 4: Display the vocabulary
print("Vocabulary:")
print(model.wv.index_to_key)

# Step 5: Display the learned embedding
word = "learning"

print(f"\nEmbedding for '{word}':")
print(model.wv[word])

print("\nEmbedding dimensions:")
print(len(model.wv[word]))

# Step 6: Predict words similar to the target word
print(f"\nWords similar to '{word}':")

for similar_word, similarity in model.wv.most_similar(
    word, topn=5
):
    print(f"{similar_word}: {similarity:.4f}")
//

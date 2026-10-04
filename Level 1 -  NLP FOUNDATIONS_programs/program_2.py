import re
import random

sentences = [
    "I love machine learning",
    "I love deep learning",
    "Machine learning is powerful",
    "Deep learning uses neural networks",
    "Python is useful for machine learning"
]


# Step 1: Preprocess the sentences
processed_sentences = []

for sentence in sentences:

    sentence = sentence.lower()

    sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)

    words = sentence.split()

    processed_sentences.append(words)


# Step 2: Build vocabulary
vocabulary = set()

for words in processed_sentences:
    for word in words:
        vocabulary.add(word)

vocabulary = sorted(vocabulary)

print("Vocabulary:")
print(vocabulary)


# Step 3: Create a dense vector for every word
embedding_dimension = 4

word_embeddings = {}

for word in vocabulary:

    vector = []

    for _ in range(embedding_dimension):
        value = round(random.uniform(-1, 1), 3)
        vector.append(value)

    word_embeddings[word] = vector


# Step 4: Display word embeddings
print("\nWord Embeddings:")

for word, vector in word_embeddings.items():

    print(f"{word:<12} : {vector}")

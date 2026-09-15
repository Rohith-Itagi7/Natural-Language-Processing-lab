import re

documents = [
    "I love machine learning",
    "I love Python programming",
    "Python is useful for machine learning"
]

# Step 1: Preprocess each document
processed_documents = []

for document in documents:
    document = document.lower()
    document = re.sub(r'[^a-zA-Z\s]', '', document)
    words = document.split()
    processed_documents.append(words)

# Step 2: Build vocabulary
vocabulary = set()

for words in processed_documents:
    for word in words:
        vocabulary.add(word)

# Sort vocabulary so the vector positions remain consistent
vocabulary = sorted(vocabulary)

print("Vocabulary:")
print(vocabulary)

# Step 3: Create BoW vector for each document
bow_vectors = []

for words in processed_documents:

    vector = []

    for word in vocabulary:
        count = words.count(word)
        vector.append(count)

    bow_vectors.append(vector)

# Step 4: Display the BoW representation
print("\nBag of Words:")

for i, vector in enumerate(bow_vectors):
    print(f"Document {i + 1}: {vector}")

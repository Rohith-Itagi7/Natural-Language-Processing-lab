import re
import math

documents = [
    "I love machine learning",
    "I love deep learning",
    "I enjoy playing cricket"
]

# 1. Preprocess documents
processed_documents = []

for document in documents:
    document = document.lower()
    document = re.sub(r'[^a-zA-Z\s]', '', document)
    words = document.split()
    processed_documents.append(words)


# 2. Build vocabulary
vocabulary = set()

for document in processed_documents:
    for word in document:
        vocabulary.add(word)

vocabulary = sorted(vocabulary)

print("Vocabulary:")
print(vocabulary)


# 3. Convert documents into vectors
vectors = []

for document in processed_documents:

    vector = []

    for word in vocabulary:
        vector.append(document.count(word))

    vectors.append(vector)


print("\nDocument Vectors:")

for i, vector in enumerate(vectors):
    print(f"Document {i + 1}: {vector}")


# 4. Cosine Similarity function
def cosine_similarity(vector1, vector2):

    # Dot product
    dot_product = 0

    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    # Magnitude of vector 1
    magnitude1 = 0

    for value in vector1:
        magnitude1 += value ** 2

    magnitude1 = math.sqrt(magnitude1)

    # Magnitude of vector 2
    magnitude2 = 0

    for value in vector2:
        magnitude2 += value ** 2

    magnitude2 = math.sqrt(magnitude2)

    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


# 5. Compare documents
print("\nCosine Similarity:")

for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):

        similarity = cosine_similarity(
            vectors[i],
            vectors[j]
        )

        print(
            f"Document {i + 1} vs Document {j + 1}: "
            f"{similarity:.3f}"
        )

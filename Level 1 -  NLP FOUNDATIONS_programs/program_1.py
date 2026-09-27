import re

sentences = [
    "I love machine learning",
    "I love Python",
    "Python is useful"
]

# Step 1: Preprocess the sentences
processed_sentences = []

for sentence in sentences:
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
    words = sentence.split()

    processed_sentences.append(words)


# Step 2: Build the vocabulary
vocabulary = set()

for words in processed_sentences:
    for word in words:
        vocabulary.add(word)

vocabulary = sorted(vocabulary)

print("Vocabulary:")
print(vocabulary)


# Step 3: Create one-hot encoding for each word
one_hot_vectors = {}

vocab_size = len(vocabulary)

for i, word in enumerate(vocabulary):

    vector = [0] * vocab_size

    vector[i] = 1

    one_hot_vectors[word] = vector


# Step 4: Display the one-hot vectors
print("\nOne-Hot Encoding:")

for word, vector in one_hot_vectors.items():
    print(word, ":", vector)

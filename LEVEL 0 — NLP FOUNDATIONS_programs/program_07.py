import re
import math

documents = [
    "I love machine learning",
    "I love Python programming",
    "Python is useful for machine learning"
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

for words in processed_documents:
    for word in words:
        vocabulary.add(word)

vocabulary = sorted(vocabulary)

print("Vocabulary:")
print(vocabulary)


# 3. Calculate TF
def calculate_tf(word, document):
    word_count = document.count(word)
    total_words = len(document)

    return word_count / total_words


# 4. Calculate IDF
def calculate_idf(word, documents):
    total_documents = len(documents)

    documents_containing_word = 0

    for document in documents:
        if word in document:
            documents_containing_word += 1

    return math.log(total_documents / documents_containing_word)


# 5. Calculate TF-IDF
print("\nTF-IDF Values:\n")

for i, document in enumerate(processed_documents):

    print(f"Document {i + 1}:")

    for word in vocabulary:

        tf = calculate_tf(word, document)

        idf = calculate_idf(word, processed_documents)

        tf_idf = tf * idf

        print(
            f"{word:<12} "
            f"TF = {tf:.3f}  "
            f"IDF = {idf:.3f}  "
            f"TF-IDF = {tf_idf:.3f}"
        )

    print()

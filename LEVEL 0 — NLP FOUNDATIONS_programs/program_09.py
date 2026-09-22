import re
import math
from collections import Counter

# Training data
texts = [
    "Python is a programming language",
    "Machine learning is a branch of artificial intelligence",
    "Deep learning uses neural networks",
    "The cricket team won the match",
    "The football player scored a goal",
    "India won the cricket match"
]

labels = [
    "Technology",
    "Technology",
    "Technology",
    "Sports",
    "Sports",
    "Sports"
]


# ---------------------------------------
# 1. Text preprocessing
# ---------------------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.split()


processed_texts = []

for text in texts:
    processed_texts.append(preprocess(text))


# ---------------------------------------
# 2. Build vocabulary
# ---------------------------------------

vocabulary = set()

for words in processed_texts:
    for word in words:
        vocabulary.add(word)

vocabulary = sorted(vocabulary)


# ---------------------------------------
# 3. Calculate TF-IDF
# ---------------------------------------

def calculate_idf(word):

    total_documents = len(processed_texts)

    documents_containing_word = 0

    for document in processed_texts:
        if word in document:
            documents_containing_word += 1

    return math.log(
        total_documents / (1 + documents_containing_word)
    )


def calculate_tfidf(document):

    vector = []

    total_words = len(document)

    for word in vocabulary:

        tf = document.count(word) / total_words

        idf = calculate_idf(word)

        tfidf = tf * idf

        vector.append(tfidf)

    return vector


training_vectors = []

for document in processed_texts:
    training_vectors.append(calculate_tfidf(document))


# ---------------------------------------
# 4. Naive Bayes classifier
# ---------------------------------------

classes = set(labels)


# Count words for each class
class_word_counts = {}
class_total_words = {}

for category in classes:

    class_word_counts[category] = Counter()
    class_total_words[category] = 0

    for words, label in zip(processed_texts, labels):

        if label == category:

            for word in words:
                class_word_counts[category][word] += 1
                class_total_words[category] += 1


# ---------------------------------------
# 5. Predict function
# ---------------------------------------

def predict(text):

    words = preprocess(text)

    scores = {}

    for category in classes:

        # Start with prior probability
        category_count = labels.count(category)

        score = math.log(
            category_count / len(labels)
        )

        total_words = class_total_words[category]
        vocabulary_size = len(vocabulary)

        for word in words:

            word_count = class_word_counts[category][word]

            # Laplace smoothing
            probability = (
                word_count + 1
            ) / (
                total_words + vocabulary_size
            )

            score += math.log(probability)

        scores[category] = score

    return max(scores, key=scores.get)


# ---------------------------------------
# 6. Test the classifier
# ---------------------------------------

test_sentences = [
    "Python programming is powerful",
    "The cricket player scored a goal",
    "Machine learning uses computers"
]

for sentence in test_sentences:

    prediction = predict(sentence)

    print("Text:", sentence)
    print("Predicted Category:", prediction)
    print()

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# ---------------------------------------
# 1. Training data
# ---------------------------------------

texts = [
    "I love this product",
    "This product is amazing",
    "The movie was excellent",
    "I really enjoyed this experience",
    "The service was wonderful",

    "I hate this product",
    "This product is terrible",
    "The movie was boring",
    "I really disliked this experience",
    "The service was horrible",

    "The product arrived today",
    "The movie starts at 7 PM",
    "The service is available today",
    "I received the product yesterday",
    "The meeting is scheduled for tomorrow"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",

    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative",

    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral",
    "Neutral"
]


# ---------------------------------------
# 2. Text preprocessing
# ---------------------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


cleaned_texts = []

for text in texts:
    cleaned_texts.append(preprocess(text))


# ---------------------------------------
# 3. Convert text into TF-IDF vectors
# ---------------------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(cleaned_texts)


# ---------------------------------------
# 4. Train the classifier
# ---------------------------------------

model = LogisticRegression()

model.fit(X, labels)


# ---------------------------------------
# 5. Predict sentiment
# ---------------------------------------

test_sentences = [
    "The product was amazing",
    "I hated this movie",
    "The product arrived today",
    "This was a wonderful experience",
    "The service was terrible"
]


for sentence in test_sentences:

    cleaned_sentence = preprocess(sentence)

    vector = vectorizer.transform([cleaned_sentence])

    prediction = model.predict(vector)[0]

    print("Text:", sentence)
    print("Sentiment:", prediction)
    print()

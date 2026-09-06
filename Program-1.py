import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Run these once
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

text = "Natural Language Processing is amazing! It helps computers understand human languages."

# 1. Lowercase
text = text.lower()

# 2. Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# 3. Tokenization
tokens = word_tokenize(text)

# 4. Remove stopwords
stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in tokens
    if word not in stop_words
]

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nAfter Stopword Removal:")
print(filtered_words)

print("\nAfter Lemmatization:")
print(lemmatized_words)

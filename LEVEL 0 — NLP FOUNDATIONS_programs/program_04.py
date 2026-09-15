import re
from collections import Counter

text = """
Natural Language Processing is a field of Artificial Intelligence.
NLP helps computers understand human language.
Natural language processing is used in chatbots, search engines,
and many other AI applications.
"""

# 1. Convert text to lowercase
text = text.lower()

# 2. Remove punctuation
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 3. Tokenize the text
words = text.split()

# 4. Remove stopwords
stop_words = {
    "is", "a", "of", "and", "the", "in", "to", "many", "other"
}

filtered_words = [
    word for word in words
    if word not in stop_words
]

# 5. Count word frequency
word_frequency = Counter(filtered_words)

# 6. Sort by frequency
sorted_frequency = sorted(
    word_frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

# 7. Display results
print("Word Frequency:\n")

for word, frequency in sorted_frequency:
    print(f"{word}: {frequency}")

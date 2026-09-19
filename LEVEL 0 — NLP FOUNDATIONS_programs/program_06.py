import re

text = """
I love learning natural language processing.
Natural language processing is interesting.
"""

# 1. Convert to lowercase
text = text.lower()

# 2. Remove punctuation
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 3. Tokenize
words = text.split()


# Function to generate n-grams
def generate_ngrams(words, n):
    ngrams = []

    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i + n])
        ngrams.append(ngram)

    return ngrams


# Generate Unigrams
unigrams = generate_ngrams(words, 1)

# Generate Bigrams
bigrams = generate_ngrams(words, 2)

# Generate Trigrams
trigrams = generate_ngrams(words, 3)


# Display results
print("Unigrams:")
for gram in unigrams:
    print(gram)

print("\nBigrams:")
for gram in bigrams:
    print(gram)

print("\nTrigrams:")
for gram in trigrams:
    print(gram)

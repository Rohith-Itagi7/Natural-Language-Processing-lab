# Regex based Text cleaning
import re

text = """Hey @Rohith! Check https://example.com #NLP2026.
Email me at test@gmail.com. I have 100 NLP projects!!!"""

# 1. Convert to lowercase
text = text.lower()

# 2. Remove URLs
text = re.sub(r'https?://\S+|www\.\S+', '', text)

# 3. Remove email addresses
text = re.sub(r'\S+@\S+\.\S+', '', text)

# 4. Remove @mentions
text = re.sub(r'@\w+', '', text)

# 5. Remove # symbol but keep the hashtag word
text = re.sub(r'#(\w+)', r'\1', text)

# 6. Remove numbers
text = re.sub(r'\d+', '', text)

# 7. Remove special characters and punctuation
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 8. Remove extra whitespace
text = re.sub(r'\s+', ' ', text).strip()

print(text)

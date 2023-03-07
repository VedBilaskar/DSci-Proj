import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is some sample text to demonstrate stopword removal."

# Tokenize the text into words
words = word_tokenize(text)

# Get the list of English stopwords from NLTK
stop_words = set(stopwords.words('english'))

# Filter out the stopwords from the list of words
filtered_words = [word for word in words if word.casefold() not in stop_words]

# Print the filtered words
print(filtered_words)

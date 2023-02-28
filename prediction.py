import csv
import spaCy

# Load the English language model
nlp = spaCy.load("en_core_web_sm")

# Define a function to lemmatize a word
def lemmatize_word(word):
    doc = nlp(word)
    return doc[0].lemma_

# Define a function to classify tweets
def classify_tweet(tweet):
    # Define lists of positive and negative words
    positive_words = ["good", "great", "awesome", "fantastic"]
    negative_words = ["bad", "terrible", "awful", "horrible"]
    
    # Tokenize the tweet into words
    preword = tweet.lower().split()
    words = lemmatize_word(preword)
    # Count the number of positive and negative words in the tweet
    num_positive_words = sum([1 for word in words if word in positive_words])
    num_negative_words = sum([1 for word in words if word in negative_words])
    
    # Classify the tweet as positive or negative based on the number of positive and negative words
    if num_positive_words > num_negative_words:
        return "positive"
    elif num_positive_words < num_negative_words:
        return "negative"
    else:
        return "neutral"

# Read the inputs from a CSV file
with open("input.csv", "r") as input_file:
    csv_reader = csv.reader(input_file)
    next(csv_reader) # Skip the header row
    inputs = [row[0] for row in csv_reader]

# Classify the tweets
outputs = [classify_tweet(tweet) for tweet in inputs]

# Write the outputs to a CSV file
with open("output.csv", "w") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Input", "Output"]) # Write the header row
    for i in range(len(inputs)):
        csv_writer.writerow([inputs[i], outputs[i]])

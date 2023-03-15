import csv
import re
import emoji
import os
import spacy


emoji_to_emotion = {
    ":grinning_face:": "happy",
    ":red_heart:": "love",
    ":angry_face:": "angry",
    ":crying_face:": "sad",
    ":face_with_open_mouth:": "surprised"
}


def tokenize(text):

    #0. handling emojis
    text  = emoji.demojize(text)
    text = re.sub(r":grinning_face:" , "happy", text)
    text = re.sub(r":red_heart:" , "love", text)
    text = re.sub(r":angry_face:" , "angry", text)
    text = re.sub(r":thumbs_down:" , "bad", text)
    text = re.sub(r":ok_hand:" , "nice", text)
    text = re.sub(r":clap:" , "awesome", text)
    text = re.sub(r":thumbs_up:" , "good", text)
    print(text)
    
    
    #1. removing quotes and ':'	
    text = re.sub(r"([\"“”:])", "", text)

    #2. (i) separate clitics into component words
    text = re.sub(r"'m", " am", text)
    text = re.sub(r"'d", " would", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"'ll", " will", text)
    text = re.sub(r"'ve", " have", text)
    text = re.sub(r"'re", " are", text)    
    # (ii) convert word-ending apostrophes to apostrophe s
    text = re.sub(r"'s ", " 's ", text)
    text = re.sub(r"s' ", "s 's ", text)
    #text = re.sub(r"([A-Za-z]+)'([A-Za-z]+)", r"\1'\2", text)
    #text = re.sub(r"([A-Za-z]+)'$", r"\1's", text)
    
    #3. separate hashtags and user references
    text = re.sub(r"#(\w+)", r"# \1", text)
    text = re.sub(r"@(\w+)", r"@ \1", text)
    
    #4. emojis to words
    
    
    #5. merge words with spaces
    text = re.sub(r"\b([A-Za-z]\.)\s+([A-Za-z]\.)\s+([A-Za-z]\.)\b", r"\1\2\3", text)
    text = re.sub(r"\b([A-Za-z]\.)\s+([A-Za-z]\.)\b", r"\1\2", text)
    
    #6. removing "....." and replacing with a space
    text = re.sub(r"\.{2,}", " ", text)
    
    
    #return text
    
    
    # split on whitespace and punctuation (except apostrophes and full stops)
    tokens = re.findall(r"[\w']+(?:[^\w\s]+[\w']+)*|[^\w\s.]+(?:\s+[A-Za-z]\.)?", text)
    
    # add final full stop if sentence ends with an abbreviation
    if tokens and tokens[-1].endswith('.') and len(tokens[-1]) <= 4:
        tokens[-1] += '.'
    return tokens



def lemmatize(text):
	
	nlp = spacy.load('en_core_web_sm')

	#string = "The service was very good and tasty food am liking it soooo much walking"

	doc = nlp(text)
	lemmatized_string = " ".join([token.lemma_ for token in doc])

	return lemmatized_string


def stopword_removal(text):
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize


    # Tokenize the text into words
    words = word_tokenize(text)

    # Get the list of English stopwords from NLTK
    stop_words = set(stopwords.words('english'))

    # Filter out the stopwords from the list of words
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Return the filtered words
    return filtered_words


with open('data.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for row in reader:
        # tokenize text in each row
        #tokens = []
        i = 2
        for text in row:
            # tokenize text
            tokens = tokenize(text)
            tokens = lemmatize(text)
            tokens = stopword_removal(text)
            #print(i , " - " , tokens , "--")
            #i+=1
            
            # join tokens with a space character and write to a single column in the output CSV file
        writer.writerow([' '.join(tokens)])
        
    

os.system("xdg-open output.csv")

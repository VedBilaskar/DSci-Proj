import csv
import re
def tokenize(text):
    # separate clitics into component words
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"'m", " am", text)
    text = re.sub(r"'ll", " will", text)
    text = re.sub(r"'ve", " have", text)
    text = re.sub(r"'d", " would", text)
    text = re.sub(r"'re", " are", text)
    # convert word-ending apostrophes to apostrophe s
    text = re.sub(r"([A-Za-z]+)'([A-Za-z]+)", r"\1'\2", text)
    text = re.sub(r"([A-Za-z]+)'$", r"\1's", text)
    # separate hashtags and user references
    text = re.sub(r"#(\w+)", r"# \1", text)
    text = re.sub(r"@(\w+)", r"@ \1", text)
    # convert dates into canonical format
    text = re.sub(r"(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})", r"CF:D:\3-\1-\2", text)
    text = re.sub(r"(\d{2,4})[/-](\d{1,2})[/-](\d{1,2})", r"CF:D:\1-\2-\3", text)
    text = re.sub(r"(\d{1,2})(?:st|nd|rd|th)? (?:of )?([A-Za-z]+) (\d{2,4})", r"CF:D:\3-\2-\1", text, flags=re.IGNORECASE)
    #text = re.sub(r"([A-Za-z]+) ?'(\d{2,4})", r"CF:D:\2-\1", text)
    #text = re.sub(r"([A-Za-z]+)", r"CF:D:????-\1", text)
    # convert times into canonical format
    text = re.sub(r"(\d{1,2}) ?([ap]m)(?: ([A-Za-z]+(?: ?[Ss][Tt])?))?", r"CF:T:\g<1>00\2:\3", text, flags=re.IGNORECASE)
    text = re.sub(r"([A-Za-z]+(?: ?[Ss][Tt])?) (\d{1,2})(?::(\d{1,2}))? ?([ap]m)?", r"CF:T:\2\3\4:\1", text, flags=re.IGNORECASE)
    # merge words with spaces
    text = re.sub(r"\b([A-Za-z]\.)\s+([A-Za-z]\.)\s+([A-Za-z]\.)\b", r"\1\2\3", text)
    text = re.sub(r"\b([A-Za-z]\.)\s+([A-Za-z]\.)\b", r"\1\2", text)
    # split on whitespace and punctuation (except apostrophes and full stops)
    tokens = re.findall(r"[\w']+(?:[^\w\s]+[\w']+)*|[^\w\s.]+(?:\s+[A-Za-z]\.)?", text)
    # add final full stop if sentence ends with an abbreviation
    if tokens and tokens[-1].endswith('.') and len(tokens[-1]) <= 4:
        tokens[-1] += '.'
    return tokens



with open('data.csv','rb') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for row in reader:
        # tokenize text in each row
        tokens = []
        for text in row:
            # tokenize text
            tokens += tokenize(text)
        writer.writerow(tokens)
    

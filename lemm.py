import spacy

nlp = spacy.load('en_core_web_sm')

string = "The service was very good and tasty food am liking it soooo much walking"

doc = nlp(string)

lemmatized_string = " ".join([token.lemma_ for token in doc])

print(lemmatized_string)


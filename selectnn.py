import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

example = "This is a sample sentence, showing off the stop words filtration.!"
word_tokens = wordnet_lemmatizer(example)
pos = nltk.pos_tag(word_tokens)
selective_pos = ['NN', 'VB']
selective_pos_words = []
for word, tag in pos:
     if tag in selective_pos:
         selective_pos_words.append((word, tag))
print(selective_pos_words)
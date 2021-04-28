import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

import string

text = input("Enter the Query ")
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_word = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_word = []
for word in tokenized_word:
    if word not in stop_words:
        final_word.append(word)

print(tokenized_word)
print(final_word)

filtered_tokens_Array = []
for item in final_word:
    words = wordnet_lemmatizer.lemmatize(item)

    filtered_tokens_Array.append(words)

print(filtered_tokens_Array)

# POS tagging
pos = nltk.pos_tag(filtered_tokens_Array)
print(pos)

# Parser
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos)
print(result)
result.draw()

selective_pos = ['NN', 'JJ']
selective_pos_words = []
for word, tag in pos:
    if tag in selective_pos:
        selective_pos_words.append((word))
print(selective_pos_words)

emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            emotion_list.append(emotion)

print(emotion_list)


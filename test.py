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
filenames = ["tables.txt", "attributes.txt", "aggregation.txt"]

for filename in filenames:
 with open(filename) as infile:
    for line in infile:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            emotion_list.append(emotion)


print(emotion_list)

table = []
attr = []
aggri = []
with open('tables.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            table.append(emotion)


with open('attributes.txt', 'r') as file2:
    for line in file2:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            attr.append(emotion)

with open('aggregation.txt', 'r') as file3:
    for line in file3:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in selective_pos_words:
            aggri.append(emotion)


print("select" + " (" + ' '.join(str(x) for x in aggri) + " )" + ' '.join(str(x) for x in attr))
print("from" + ' '.join(str(x) for x in table))


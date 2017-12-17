import nltk
from texts import Texts

split_test = nltk.parag_tokenize(Texts.gettysburg_address)

for sentence in split_test:
    print(sentence)

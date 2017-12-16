import nltk

from texts import Texts

split_test = nltk.sent_tokenize(Texts.gettysburg_address)

for sentence in split_test:
    print(sentence)

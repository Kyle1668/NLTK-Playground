import nltk
from texts import Texts
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


def process_content(argued_text):
    for sentence in argued_text:
        words = word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        print(tagged)


def main():
    sample_text = sent_tokenize(Texts.sample_movie_review)
    process_content(sample_text)

main()


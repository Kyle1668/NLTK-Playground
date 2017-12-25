from texts import Texts
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

porter_algorithm = PorterStemmer()
stop_words = set(stopwords.words("English"))

non_stop_text = []
target_text = word_tokenize(Texts.sample_movie_review)

for word in target_text:
    if word not in stop_words:
        word = porter_algorithm.stem(word)
        non_stop_text.append(word)

print(target_text)
print(non_stop_text)

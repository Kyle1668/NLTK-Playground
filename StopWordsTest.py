from texts import Texts
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

gettysburg_address = word_tokenize(Texts.gettysburg_address)
stop_words = set(stopwords.words("English"))
sanitized_gettysburg_address = []

for word in gettysburg_address:
    if word not in stop_words:
        sanitized_gettysburg_address.append(word)

print(sanitized_gettysburg_address)

# ['Four', 'score', 'seven', 'years', 'ago', 'fathers', 'brought', 'forth', 'continent', ','
# , 'new', 'nation', ',', 'conceived', 'Liberty', ',', 'dedicated', 'proposition', 'men', '
# created', 'equal', '.', 'Now', 'engaged', 'great', 'civil', 'war', ',', 'testing',
# 'whether', 'nation', ',', 'nation', 'conceived', 'dedicated', ',', 'long',
# 'endure', '.', 'We', 'met', 'great', 'battle-field', 'war', '.', 'We',
# 'come', 'dedicate', 'portion', 'field', ',', 'final', 'resting', 'place'] ...

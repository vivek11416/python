
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
text = "Good Morning! How are You ! Doing yours ?"
sent_toke_text = sent_tokenize(text)
word_toke_text = word_tokenize(text)
# print(sent_toke_text)
# print(word_toke_text)

from nltk.corpus import stopwords

print(stopwords.words('english'))

toke_without_stop = [word for word in word_toke_text if not word in stopwords.words()]
print(toke_without_stop)
from __future__ import print_function
import re
import nltk.tokenize

fin = open("EG 273 - German only.txt", 'r', encoding='utf-8')
data = fin.read()

sentences = nltk.tokenize.sent_tokenize(data)

for s in sentences:
    s = re.sub('\s+',' ', s)
    print(s)
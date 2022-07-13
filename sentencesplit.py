from __future__ import print_function
import re
import nltk.tokenize
from sqlalchemy import insert

from main import session
from models import Sentence

"""def split_file():
    finpath = input("Input the exact path of the file which you would like to split into sentences\n")
    fin = open(finpath, 'r', encoding='utf-8')
    data = fin.read()
    foutpath = input("Input the name of the file which you would like the sentences to be split into\n")
    fout = open(foutpath, 'w', encoding='utf-8')

    sentences = nltk.tokenize.sent_tokenize(data)
    for s in sentences:
        s = re.sub('\s+',' ', s)
        fout.write(s + '\n')

    fin.close()
    fout.close()"""


def split_file():
    finpath = input("Input the exact path of the file which you would like to split into sentences\n")
    fin = open(finpath, 'r', encoding='utf-8')
    data = fin.read()
    sntncs = nltk.tokenize.sent_tokenize(data)
    for s in sntncs:
        s = re.sub('\s+', ' ', s)
        word_count = len(s.split())
        sen = Sentence(sentence=s, word_count=word_count)
        session.add(sen)
        session.commit()


from __future__ import print_function
import re
import nltk.tokenize
from main import session
from models import Sentence


# takes file path from user and splits file into sentences, then stores in database
def split_file():
    # get file path and read file
    finpath = input("Input the exact path of the file which you would like to split into sentences\n")
    fin = open(finpath, 'r', encoding='utf-8')
    data = fin.read()

    # tokenizes file of sentences into sentences
    sntncs = nltk.tokenize.sent_tokenize(data)
    for s in sntncs:
        # removes duplicate spaces in string
        s = re.sub('\s+', ' ', s)

        # obtain word count of sentences
        word_count = len(s.split())

        # write formatted sentence to database
        sen = Sentence(sentence=s, word_count=word_count)
        session.add(sen)
        session.commit()


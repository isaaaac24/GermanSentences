from __future__ import print_function
import re
import nltk.tokenize

def split_file():
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
    fout.close()
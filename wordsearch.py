from main import session
from models import Sentence


# find all sentences that contain the user specified word
def find_all(search_term):
    sen_all = session.query(Sentence).filter(Sentence.sentence.contains(search_term)).all()
    for sen in sen_all:
        print(sen.sentence)


# find the first sentence in the database which contains an example of the user specified word
def first_sen(search_term):
    sen = session.query(Sentence).filter(Sentence.sentence.contains(search_term)).first()
    print(sen.sentence)


# perform a custom search
def custom_search(search_term):
    word_count = int(input("What is the minimum amount of words in the sentence?"))

    # query to return all sentences that contain the user specified word and with the minimum amount of words specified
    query = session.query(Sentence).filter(
        Sentence.word_count >= word_count,
        Sentence.sentence.contains(search_term)
    ).all()

    for sen in query:
        print(sen.sentence)

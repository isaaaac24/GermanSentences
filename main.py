# import database items
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database
engine = db.create_engine('mysql://root:Wrightson6534@localhost:3306/sentences')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# create database
# Base.metadata.create_all(engine)

# import other files, must be after database import else circular import
import sentencesplit, wordsearch

# menu options as dictionaries to simplify appearance
menu_options = {
    1: 'Split file into sentences',
    2: 'Find a sentence containing a word',
    3: 'Exit',
}

find_menu_options = {
    1: 'Find all instances of a word',
    2: 'Find first instance of a word',
    3: 'Custom search'
}


# prints options for appropriate menu from dictionary
def print_options(chosen_menu):
    for key in chosen_menu.keys():
        print(key, '--', chosen_menu[key])


# first menu option
def menu_split():
    sentencesplit.split_file()


# second menu option
def menu_search():
    print("What kind of search would you like to perform?")
    while True:
        # op_status states whether an operation has been completed or not
        op_status = False

        print_options(find_menu_options)

        option_search = int(input("Enter your choice\n"))
        if option_search == 1:
            wordsearch.search_word(option_search)
            op_status = True
        elif option_search == 2:
            wordsearch.search_word(option_search)
            op_status = True
        elif option_search == 3:
            wordsearch.search_word(option_search)
            op_status = True
        elif option_search == 4:
            print('Thank you for using LangIO!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
            continue

        # if an operation has completed, reprint hello text and return to main menu
        if op_status:
            print("Hello, welcome to LangIO")
            break


# main function, displays main menu
if __name__ == '__main__':
    print("Hello, welcome to LangIO")

    while True:
        print_options(menu_options)
        option_main = int(input("Enter your choice\n"))
        if option_main == 1:
            menu_split()
        elif option_main == 2:
            menu_search()
        elif option_main == 3:
            print('Thank you for using LangIO!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')

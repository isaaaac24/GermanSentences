import sentencesplit, wordsearch

menu_options = {
    1: 'Split file into sentences',
    2: 'Find a sentence containing a word',
    3: 'Exit',
}

def print_options():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def option1():
    sentencesplit.split_file()

def option2():
    wordsearch.search_word()

if __name__=='__main__':
    print("Hello, welcome to LangIO")
    while True:
        print_options()
        option = int(input("Enter your choice\n"))
        if option == 1:
            option1()
        if option == 2:
            option2()
        elif option == 3:
            print('Thank you for using LangIO!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

import sentencesplit, wordsearch

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


def print_options(chosen_menu):
    for key in chosen_menu.keys():
        print(key, '--', chosen_menu[key])


def option1():
    sentencesplit.split_file()


def option2():
    print("What kind of search would you like to perform?")
    while True:
        print_options(find_menu_options)
        option = int(input("Enter your choice\n"))
        if option == 1:
            wordsearch.search_word(option)
        if option == 2:
            wordsearch.search_word(option)
        if option == 3:
            wordsearch.search_word(option)
        elif option == 4:
            print('Thank you for using LangIO!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


if __name__=='__main__':
    print("Hello, welcome to LangIO")
    while True:
        print_options(menu_options)
        option = int(input("Enter your choice\n"))
        if option == 1:
            option1()
        if option == 2:
            option2()
        elif option == 3:
            print('Thank you for using LangIO!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')

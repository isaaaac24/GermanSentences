user_filter = {
    "num_words": 0
}


def search_word(option):
    search_term = input("Input the word you would like to search for\n")
    fpath = input("Input the address of the file you would like to search")
    f = open(fpath, 'r', encoding='utf-8')
    if option == 1:
        sen_all = find_all(search_term, f)
        for sen in sen_all:
            print(sen)
    elif option == 2:
        print(first_sen(search_term, f))
    elif option == 3:
        sen_all = find_all(search_term, f)
        min_words = input("What is the minimum length of your sentence?\n")
        num_sen = input("How many sentences would you like?\n")
        results = (custom_search(sen_all, min_words, num_sen))
        for sen in results:
            print(sen)


def find_all(search_term, f):
    sen_all = []
    for line in f:
        if search_term in line:
            sen_all.append(line)
    return sen_all


def first_sen(search_term, f):
    for line in f:
        if search_term in line:
            return line


def custom_search(sen_all, min_words, num_sen):
    user_filter["num_words"] = min_words
    results = []
    for sen in sen_all:
        word_list = sen.split()
        if (len(word_list) > int(min_words)):
            results.append(sen)
        if len(results) == int(num_sen):
            return results
    return results

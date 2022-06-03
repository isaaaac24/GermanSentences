def search_word():
    search_term = input("Input the word you would like to search for\n")
    fpath = input("Input the address of the file you would like to search")
    f = open(fpath, 'r', encoding='utf-8')
    for line in f:
        if (search_term in line):
            print(line)

with open("books/frankenstien.txt") as f:
    file_contents = f.read()
    word_list = file_contents.split()
    words = 0
    while len(word_list) > 0:
        words += 1
        word_list.pop()
    print(words)
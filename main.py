def main():
    path = "books/frankenstien.txt"
    word_list = get_book_word_list(path)
    print_report(word_list, path)

def print_report(word_list, path):
    print(f"Begining report for {path}...\nThere are {get_num_words(word_list)} words in the book\n\n")
    dict = count_letters(word_list)
    for letter in dict:
        if letter.isalpha():
            print(f"The letter {letter} appears {dict[letter]} times in the book...")
    print("End of report!")


def get_num_words(word_list):
    return len(word_list.split())

def count_letters(word_list):
    word_list = list(word_list.lower())
    times = {}
    for char in word_list:
        if char not in times:
            times[char] = 1
        else:
            times[char] += 1
    return times

def get_book_word_list(path):
    with open(path) as f:
        return f.read()

main()
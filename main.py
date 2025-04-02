from stats import *

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    
def pretty_print_characters(sorted_letters):
    print("-------- Character Count --------")
    for set in sorted_letters:
        print(f'{set[0]}: {set[1]}')

def main():
    print("========== BOOKBOT ==========")
    book = "./books/frankenstein.txt"
    print(f'Analyzing book found at {book}...')
    text = get_book_text(book)
    num_words = total_words(text)
    print('---------- Word Count ----------\n'
           f'Found {num_words} total words')
    num_letters = letter_count(text)
    sorted_letters = sort_dict(num_letters)
    pretty_print_characters(sorted_letters)
    print("========== END ==========")
if __name__ == "__main__":
    main()

from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text
    
def pretty_print_characters(sorted_letters):
    for set in sorted_letters:
        print(f'{set[0]}: {set[1]}')

def main(path):
    book = path
    print("========== BOOKBOT ==========")
    print(f'Analyzing book found at {book}...')
    print('---------- Word Count ----------')

    text = get_book_text(book)
    num_words = total_words(text)
    print(f'Found {num_words} total words')

    num_letters = letter_count(text)
    sorted_letters = sort_dict(num_letters)
    
    print("-------- Character Count --------")
    pretty_print_characters(sorted_letters)
    print("========== END ==========")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        main(args[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

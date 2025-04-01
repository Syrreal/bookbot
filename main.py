from stats import *

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def main():
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    num_words = total_words(text)
    num_letters = letter_count(text)
    print(f'{num_words} words found in the document')
    print(num_letters)

if __name__ == "__main__":
    main()

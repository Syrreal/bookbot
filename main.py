
def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def main():
    book = "./books/frankenstein.txt"
    print(get_book_text(book))

if __name__ == "__main__":
    main()

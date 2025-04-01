
def total_words(text):
    num_words = len(text.split())
    return num_words

def letter_count(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:

        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict
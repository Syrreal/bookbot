
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

def sort_dict(dict):
    sorted = [(key, value) for key, value in dict.items() if key.isalpha()]
    sorted.sort(reverse=True, key=lambda x: x[1])
    return sorted
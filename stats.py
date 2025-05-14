def get_word_count(book_text):
    word_count = book_text.split()
    return len(word_count)

def get_char_count(book_text):
    char_count = {}
    for char in book_text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_char_count(char_count):
    sort_char_list = []
    for char in char_count:
        sort_char_list.append({"char": char, "num": char_count[char]})

    sort_char_list.sort(reverse=True, key=sort_on)
    return sort_char_list
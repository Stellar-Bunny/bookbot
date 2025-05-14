import sys

def get_book_text(book_path):
    with open(book_path) as t:
        text = t.read()

    return text

from stats import get_word_count, get_char_count, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sort_char = sort_char_count(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sort_char:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

main()

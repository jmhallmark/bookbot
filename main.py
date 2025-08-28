import sys
from stats import (
    get_word_count, 
    get_char_count, 
    get_sorted_character_list,
)
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    script = sys.argv[0]
    book_path = sys.argv[1]
    fpath = ""
    ftext = ""
    file_contents = get_book_text(book_path)
    wordcount = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    list_of_dictionary = get_sorted_character_list(char_count)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}")
    print ("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    #print(f"{char_count}")
    print ("--------- Character Count -------")
    for item in list_of_dictionary:
        print(f"{item["char"]}: {item['num']}")
    #print(f"{list_of_dictionary}")
    sys.exit(0)
def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(file_contents):
    words = file_contents.split()
    wcount = len(words)
    return wcount

main()

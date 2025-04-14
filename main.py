from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def print_report(filepath, num_words, sorted_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 1:
        print("No filepath was entered")
        print("Please use the following format:")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = count_words(file_contents)
    num_characters = count_characters(file_contents)
    sorted_count = sort_character_counts(num_characters)
    print_report(filepath, num_words, sorted_count)


main()

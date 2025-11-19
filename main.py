def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
    return text

from stats import word_counter
from stats import character_counter
from stats import sort_on

counted_words = word_counter(main())
sorted_chars = sort_on(character_counter(main))

for counted_char in sorted_chars:
    print(f"{counted_char["char"]}: {counted_char["num"]}")
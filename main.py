from stats import get_num_words, count_characters
import sys


if len(sys.argv) == 2:
    filepath = "/home/reinhardt/workspace/github.com/reinhardt007/bookbot/" + sys.argv[1]
    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def main():
        book_text = get_book_text(filepath)
        num_words = get_num_words(book_text)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        count_characters(book_text)
        print("============= END ===============")
        
    main()

    
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

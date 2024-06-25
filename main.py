def main():
    frank_path = "/home/tzscott/workspace/github.com/t-z-scott/bookbot/books/frankenstein.txt"
    text = get_book_text(frank_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the book")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

main()
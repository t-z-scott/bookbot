def main():
    frank_path = "/home/tzscott/workspace/github.com/t-z-scott/bookbot/books/frankenstein.txt"
    text = get_book_text(frank_path)
    num_words = word_count(text)
    char_count = count_chars(text)
    print(f"{num_words} words found in the book")

def count_chars(book):
    chars_dict = {}
    text_lower = book.lower()

    for character in text_lower:
        if character not in chars_dict:
            chars_dict[character] = 1
        else:
            chars_dict[character] += 1
    
    return chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

main()
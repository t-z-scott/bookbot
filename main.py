"""
Bookbot project: a script that reads public domain books as text files
    Created by @t-z-scott on GitHub
    Credit to boot.dev
"""

def main():
    frank_path = "/home/tzscott/workspace/github.com/t-z-scott/bookbot/books/frankenstein.txt"  # path to frankenstein book
    text = get_book_text(frank_path)    # text for frankenstein book as a string
    num_words = word_count(text)        # word count for frankenstein book

    char_count = count_chars(text)
    # Initialize a empty list to hold the dictionary entries as a dictionary
    char_counts_list = []
    # Loop over the original dictionary's items
    for char, count in char_count.items():
        # Create a new dictionary entry for each character and its count
        entry = {'char': char, 'num': count}
        # Add the new dictionary entry to the list
        char_counts_list.append(entry)
    
    char_counts_list.sort(reverse=True, key=sort_on)
    print(f"{num_words} words found in the book")
    print()
    for d in char_counts_list:
        print(f"The {d['char']} character was found {d['num']} times")

def count_chars(book):
    """counts the characters in the string `book`
    
    Parameters
    ----------
    book : string
        the text in a book in string format
    
    Returns
    -------
    chars_dict : dictionary
        a dictionary in the structure of character:char_count
    """
    chars_dict = {}
    text_lower = book.lower()   # lowercase all characters

    for character in text_lower:
        if character.isalpha() == True: # only alphanumeric characters
            if character not in chars_dict:
                chars_dict[character] = 1
            else:
                chars_dict[character] += 1
    
    return chars_dict

def get_book_text(path):
    """gets the words in the book specified in `path` as a string
    
    Parameters
    ----------
    path : string
        the relative or absolute file path to the book
    
    Returns
    -------
    f.read : string
        the text in the book in string format
    """
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def word_count(book):
    """counts the words in the string `book`
    
    Parameters
    ----------
    book : string
        the text in a book in string format
    
    Returns
    -------
    len(words) : integer
        number of words in the text
    """
    words = book.split()
    return len(words)

main()
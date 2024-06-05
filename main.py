def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")

    text = get_book_text(book_path)
    #print(text)
   
    word_count = get_word_count(text)
    print (f"{word_count} words found in the document")

    char_count = get_char_count(text)
    print(char_count)
    print("--- End report --- ")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_text = text.lower()
    char_dict = {}

    for char in lower_text:
        if char in char_dict:
            if char.isalpha() == 1:
                char_dict[char] += 1
        else:
                if char.isalpha() == 1:
                    char_dict[char] = 1
    return char_dict


main()

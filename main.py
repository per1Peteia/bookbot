def main():
    book_path = "books/frankenstein.txt"
    
    print(f"--- Begin report of {book_path} ---")

    text = get_book_text(book_path)
    #print(text)
   
    word_count = get_word_count(text)
    print (f"{word_count} words found in the document")

    char_dict = get_char_count(text)
    
    listed_char_dict = get_listed(char_dict)
    
    listed_char_dict.sort(reverse=True, key=sort_on)
    
    for item in listed_char_dict:
        print(f"The '{item['char']}' character was found {item['num']} times")

    #print(listed_char_dict)

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

def get_listed(char_dict):
    listed_dicts = []
    for key in char_dict:
        one_char_dict = { 'char' : key, 'num' : char_dict[key] }
        #print(one_char_dict)
        listed_dicts.append(one_char_dict)
    return listed_dicts

def sort_on(dict):
    return dict['num']


main()

def main():
        book = get_book()
        print("--Begin report--")
        get_word_count(book)
        print()
        print(get_letter_count(book))


def get_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def get_word_count(book):
    words = book.split()
    word_count = len(words)
    print(f"{word_count} words were found in the document")
    return word_count

def get_letter_count(input_string):
     letter_count = {}
     input_string = input_string.lower()
     for character in input_string:
          if character.isalpha():
               if character in letter_count:
                    letter_count[character] += 1
               else:
                    letter_count[character] = 1
     sorted_dict = sorted(letter_count.keys())
     for key in sorted_dict:
        print(f" '{key}' was found {letter_count[key]} times")
     print()
     return "--End report--"


          
main()
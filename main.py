
def count_words(text):
    return len(book_contents.split())

def get_count_chars_lowercase(text):
    count_dict = {}
    temp_text = text.lower()
    for i in range(0, len(temp_text)):
        character = temp_text[i]
        if not character.isalpha():
            continue
        elif character not in count_dict:
            count_dict[character] = 1
        else:
            count_dict[character] += 1

    return count_dict


input_file = "./books/frankenstein.txt"

with open(input_file) as f:
    book_contents = f.read()

    print(f"--- Begin report of {input_file} ---")
    print(f"{count_words(book_contents)} words found in the document")
    print("")

    character_count = dict(sorted(get_count_chars_lowercase(book_contents).items(), key=lambda item: item[1], reverse=True))
    for letter in character_count:
        print(f"The '{letter}' character was found {character_count[letter]} times")

    print("--- End report ---")

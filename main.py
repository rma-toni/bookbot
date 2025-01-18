import string

def character_count(text):
    wc_dict = dict.fromkeys(string.ascii_lowercase, 0)
    lowered_text = text.lower()
    for character in lowered_text:
        if(True):
            if (character in wc_dict):
                wc_dict[character] += 1
    return wc_dict

def main():
    ccount_set = {}
    w_count = 0

    with open("books/frankenstein.txt") as f:
              
        file_contents = f.read()
        w_count = len(file_contents.split())
        ccount_set = character_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{w_count} words found in the document\n")
    for item in ccount_set:
        print(f"The '{item}' character was fount {ccount_set[item]} times")
    print("--- End report ---")

main()
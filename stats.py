#function that counts words

def word_count_total(text: str) -> int:
    return len(text.split())

#function that counts characters (including symbols and spaces, also converts to lowercase)
def char_count_dict(text: str) -> dict:
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

#function that sorts dictionary by value
def sort_on(items):
    return items["num"]

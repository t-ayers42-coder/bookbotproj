import sys
print ("Usage: python3 main.py <path_to_book>")
file_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import word_count_total, char_count_dict, sort_on

text = get_book_text(file_path)
word_count = word_count_total(text)
char_dict = char_count_dict(text)
char_list = []

for char, count in char_dict.items():
    char_list.append({"char": char, "num": count})

char_list.sort(key=sort_on, reverse = True)


print("============ BOOKBOT ============")
print("Analyzing book found at " + file_path) 
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in char_list:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")

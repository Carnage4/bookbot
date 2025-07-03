import sys
from stats import get_book_text
from stats import get_num_words
from stats import char_count 
from stats import sorted_dict
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
text = get_book_text(sys.argv[1])
total_num = get_num_words(text)
total_char = char_count(text)
final_list = sorted_dict(text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {total_num} total words")
print("--------- Character Count -------")
for item in final_list:
    char = item["char"]
    num = item["num"]
    if char.isalpha():
        print(f"{char}: {num}")
print("============= END ===============")

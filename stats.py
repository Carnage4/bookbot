def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def get_num_words(text):
    words = len(text.split())
    return words

def char_count(text):
    count = {}
    for char in text:
        x = char.lower()
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    return count

def sorted_dict(text):
    sorted_list = []
    counts = char_count(text)
    for key in counts:
        entry = {"char": key, "num": counts[key]}
        sorted_list.append(entry)
    def sort_on(item):
        return item["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

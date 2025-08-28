
def get_word_count(file_contents):
    words = file_contents.split()
    wcount = len(words)
    return wcount

def get_char_count(file_contents):
    lc_contents = file_contents.lower()
    char_count = {}
    for i in lc_contents:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1
    return char_count

def sort_on(d):
    return d["num"]

def get_sorted_character_list(char_count):
    to_sort = []

    for key, value in char_count.items():
        if key.isalpha():
            to_sort.append({"char": key, "num": char_count[key]})
        
    to_sort.sort(reverse=True, key=sort_on)
    return to_sort
    

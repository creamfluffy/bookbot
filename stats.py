def word_counter(text):
    words_list = text.split()
    num_words = len(words_list)
    print(f"Found {num_words} total words")
    return num_words

def character_counter(text):
    char_dict = {}
    for ch in text():
        if not ch.isspace():
            ch = ch.lower()
            char_dict[ch] = char_dict.get(ch, 0) + 1
    return char_dict

def by_num(d):
    return d['num']

def sort_on(char_dict):
    ch_dict_list = []
    for ch, count in char_dict.items():
        ch_dict_list.append({"char": ch, "num": count})
    return sorted(ch_dict_list, reverse=True, key=by_num)

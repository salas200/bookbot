def num_words(text):
    sing_str = text.split()

    return len(sing_str)


def char_count(text):
    char = {}
    for t in text:
        if t.lower() in char:
            char[t.lower()] += 1
        else:
            char[t.lower()] = 1

    return char


def sort_on(dict):
    return dict["num"]


def sorted_dict(char):
    List = []
    for k , v in char.items():
        List += [{"char" : k, "num" : v}]
    List.sort(reverse=True, key=sort_on)
    
    return List




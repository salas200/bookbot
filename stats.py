def num_words(text):
    sing_str = text.split()

    return len(sing_str)

def char_count(text):
    char_count = {}
    for t in text:
        if t.lower() in char_count:
            char_count[t.lower()] += 1
        else:
            char_count[t.lower()] = 1

    return char_count

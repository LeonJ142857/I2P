def find_longest_word(lwords):
    max_length = len(lwords[0])
    for i in lwords:
        if len(i) > max_length:
            max_length = len(i)
    return max_length

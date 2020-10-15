def char_freq(string):
    frequencies = {}
    for i in string:
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1
    return frequencies


def word_frequencies(my_list):
    res = {}
    for i in my_list:
        for word in i.split():
            res.setdefault(word, 0)
            res[word] += 1
    return res

print(word_frequencies(["Hello, world.", "The world is round", "Round is the world"]))


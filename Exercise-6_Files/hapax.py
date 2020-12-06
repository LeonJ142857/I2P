import pprint as pp
import re


def word_frequencies(my_list: str):
    res = {}
    symbols = R"+!.,?:;_\"'-)(’”—"
    for word in my_list.split():
        if bool(re.match(r"^[a-zA-Z]+", word)):
            if bool(re.match(r"[a-zA-Z]+[{}]+$".format(symbols), word)):
                word = word[:re.search(r"[{}]".format(symbols), word).span()[0]].lower()
            else:
                word = word.lower()
            res[word] = res.get(word, 0) + 1
    return res


def hapax(file_name: str):
    file = open(file_name, encoding="UTF-8")
    text = file.read()
    res = []
    dictionary = word_frequencies(text)
    for k in dictionary.keys():
        if dictionary[k] == 1:
            res.append(k)
    file.close()
    return res


output = hapax(R"C:\Users\user\PycharmProjects\Tugas_Binus\I2P\Exercise6(Files)\out.txt")
pp.pprint(pp.pformat(output, compact=True, width=800))
print(len(output), "hapax legomenon words found")

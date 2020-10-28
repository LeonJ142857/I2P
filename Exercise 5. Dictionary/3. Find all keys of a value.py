def find_value(my_dict, val):
    res = []
    for k in my_dict.keys():
        if my_dict[k] == val:
            res.append(k)
    return res


print(find_value({'a': 1, 'b': 2, 'c': 0, 'd': 0}, 0))

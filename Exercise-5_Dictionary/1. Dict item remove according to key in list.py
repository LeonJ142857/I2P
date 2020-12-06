def remove_keys(my_dict, key_list):
    for i in key_list:
        my_dict.pop(i)
    return my_dict


print(remove_keys({0: 1, 1: 2, 2: 3, 3: 3}, [0, 1, 2]))

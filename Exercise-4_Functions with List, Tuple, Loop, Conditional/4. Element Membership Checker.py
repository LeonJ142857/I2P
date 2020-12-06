def is_member(val, value_list):
    for i in range(len(value_list)):
        if value_list[i] == val:
            return True
    return False

def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if j == i:
                return True
    return False

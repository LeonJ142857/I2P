def histogram(lst):
    for i in lst:
        row = ""
        for j in range(i):
            row += '*'
        print(row)

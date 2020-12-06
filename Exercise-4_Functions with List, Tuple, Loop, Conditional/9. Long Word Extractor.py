def filter_long_words(lwords, n):
    result = []
    for i in lwords:
        if len(i) > n:
            result.append(i)
    return result

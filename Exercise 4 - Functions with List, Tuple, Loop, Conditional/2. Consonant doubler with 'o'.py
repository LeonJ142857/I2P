def translate(text):
    result = ""
    for i in text:
        if i in ('a','i','u','e','o',' '):
            result += i
        else:
            result += i+'o'+i
    return result


text = str(input())
print(translate(text))

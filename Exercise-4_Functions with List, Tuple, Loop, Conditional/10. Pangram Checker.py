def pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in sentence:
        i = i.lower()
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
    if len(alphabet) == 0:
        return True
    else:
        return False

print(pangram("The quick brown fox jumps over the lazy dog."))

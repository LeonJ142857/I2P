def makeForming(verb):
    if verb.endswith("ie"):
        verb = verb[:-2]+ "ying"
    elif verb.endswith('e'):
        verb = verb[:-1] + "ing"
    elif len(verb) >= 3 and (verb[-1] and verb[-3]) not in "aiueo" and verb[-2] in "aiueo":
        verb += verb[-1]+"ing"
    else:
        verb += "ing"
    return verb

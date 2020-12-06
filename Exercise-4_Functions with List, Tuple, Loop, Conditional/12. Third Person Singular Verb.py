def makeForms(verb):
    if verb.endswith('y'):
        verb = verb[:len(verb)-1]
        verb += "ies"
    elif (verb.endswith('o') or verb.endswith('s') or verb.endswith('x') or
          verb.endswith('z') or verb.endswith('ch') or verb.endswith('sh')):
        verb += "es"
    else:
        verb += 's'
    return verb


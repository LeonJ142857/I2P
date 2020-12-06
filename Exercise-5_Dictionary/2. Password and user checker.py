def accept_login(users: dict, username: str, password: str):
    if username in users.keys() and users[username] == password:
        return True
    else:
        return False


print(accept_login({'a': 'abcd', 'b': 'cdef', 'c': 'defg'}, 'b', 'cdef'))

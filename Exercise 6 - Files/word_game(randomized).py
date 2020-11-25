import random
def word_game(word_list:list, flag:dict, possible:list, word:str):
	result = [word]
	possible = []
	for i in word_list:
		if not flag[i] and i[0] == word[-1]:
			possible.append(i)
			flag[i] = True
	return result + word_game(word_list, flag, possible, random.choice(possible)) if len(possible) != 0 else result

file = None
with open("pokemon.txt", encoding="UTF-8") as d:
	file = d.read()
word_list = file.split()
word = random.choice(word_list)
visited = {}
possible = []
for i in word_list:
	visited[i] = False
print(word_game(word_list, visited, possible, word))

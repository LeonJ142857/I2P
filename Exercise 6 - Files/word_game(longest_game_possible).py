def word_game(word, result, results, word_list, possibles):
	result = result[:]+[word]
	possibles = []
	for w in word_list:
		if w not in result and w[0] == word[-1]:
			possibles.append(w)
	if len(possibles) == 0:
		results.append(result)
		result = []
	else:
		for p in possibles:
			word_game(p, result, results, word_list, possibles)


def max(results):
	maximum = 0
	for result in results:
		if len(result) > maximum :
			maximum = len(result)
	return maximum

file = None
with open("pokemon.txt", encoding="UTF-8") as d:
	file = d.read()
word_list = file.split()
possibles, results, result = [], [], []
true_results = []
for w in word_list:
	possibles, results, result = [], [], []
	word_game(w, result, results, word_list, possibles)
	M = max(results)
	for res in results:
		if len(res) == M:
			true_results.append(res)
			break
Mtrue = max(true_results)
for w in true_results:
	if len(w) == Mtrue:
		print(w)

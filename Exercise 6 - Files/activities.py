import calendar as cal
# Part 1
file = None
with open("activities.csv", 'r', encoding="UTF-8") as d:
	file = d.read()
data = file.split('\n')
res = {}
NA: int = 0
for line in range(len(data)):
	tmp: list = data[line][1:len(data[line]) - 1].split(',')
	if line > 0:
		if tmp[0] == "NA":
			NA += 1
		elif len(tmp) == 1: break
		else:
			date: str = tmp[1].split('""')[1]
			res[date]: int = res.get(date, 0) + int(tmp[0])
sorted_data: list = sorted(list(res.values()))
n: int = len(res)
mean: int = sum(res.values()) / n
med: int = (sorted_data[n//2] if n % 2 == 1 else (sorted_data[n//2] + sorted_data[n//2 - 1]) / 2)
for k in res.keys():
	print("Date " + k + ": " + str(res[k]))

print("Mean steps per day rounded to the nearest int:", int(mean))
print("Median steps per day:", med)
print("Missing values:", NA)

# Part 2
data = file.replace('NA', '0').split('\n')
file2 = open("activities2.csv", 'w', encoding="UTF-8")
for line in range(len(data)):
	tmp: list = data[line][1:len(data[line]) - 1].split(',')
	if line == 0:
		for i in range(len(tmp)):
			result = (tmp[i] if i not in range(1,3) else '"'+tmp[i].split('""')[1]+'"')
			print(result, end=',', file=file2)
		print("day_type", file=file2)
	else:
		if len(tmp) == 1: break
		else:
			date: str = tmp[1].split('""')[1]
			tmp[1] = date
			day = cal.weekday(int(date[:4]), int(date[5:7]), int(date[8:]))
			day_type = ("Weekday" if day in range(6) else "Weekend")
			print(f'{tmp[0]},"{tmp[1]}",{tmp[2]},{day_type}', file=file2)
file2.close()




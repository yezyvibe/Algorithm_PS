skill = list(skill)
cnt = 0
for st in skill_trees:
	st = list(st)
	tmp = []
	for i in st:
		if i in skill:
			tmp.append(i)
	if len(tmp) == len(skill):
		if tmp == skill:
			cnt += 1
	else:
		for i in range(len(tmp)):
			if skill[i] != tmp[i]:
				break
		cnt += 1
	return cnt
	
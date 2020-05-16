person1 = [1,2,3,4,5]
person2 = [2,1,2,3,2,4,2,5]
person3 = [3,3,1,1,2,2,4,4,5,5]
dict = {1:0 ,2:0, 3:0}

for i in range(len(answers)):
    # 인덱스
    a = i % len(person1)
    b = i % len(person2)
    c = i % len(person3)
    if answers[i] == person1[a]:
        dict[1] += 1
    if answers[i] == person2[b]:
        dict[2] += 1
    if answers[i] == person3[c]:
        dict[3] += 1

    max_v = 0
    for key, value in dict.items():
        if value > max_v:
            if len(answer) == 0:
                max_v = value
                answer.append(key)
            else:
                answer.clear()
                max_v = value
                answer.append(key)
        elif value == max_v:
            answer.append(key)
    answer.sort()

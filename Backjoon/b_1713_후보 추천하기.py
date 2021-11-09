from collections import defaultdict

r_dic = defaultdict(int)

n = int(input())
r_cnt = int(input())
r_lst = input().split(' ')
photo = []

for item in r_lst:
    r_dic[item] += 1
    if item in photo:
        continue
    elif len(photo) < n:  # 다 차지 않은 상태
        photo.append(item)
    elif len(photo) == n:  # 꽉 차 있는 상태
        min_v = 10000
        for k in photo:
            if r_dic[k] < min_v:
                min_v = r_dic[k]
                d = k
        else:
            photo.remove(d)
            del(r_dic[d])
            photo.append(item)
photo = list(map(int, photo))
photo.sort()
print(*photo)
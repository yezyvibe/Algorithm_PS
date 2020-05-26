def dfs(l, c, k, idx):
    if (k == l):
        res_lst.append(''.join(res))
        return
    else:
        for i in range(c):
            if (visit[i] == 0 and idx <= i):
                visit[i] = 1
                res[k] = alphabets[i]
                idx = i
                dfs(l, c, k+1, idx)
                visit[i] = 0
def check(arr):
    for a in arr:
        v_cnt = 0
        c_cnt = 0
        for i in a:
            if i in vowels:
                v_cnt += 1
            if i not in vowels:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            print(a)

vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
alphabets = sorted(list(map(str, input().split())))
visit = [0]*c
res = [0]*l
res_lst = []
dfs(l, c, 0, 0)
check(res_lst)
# print(res_lst)

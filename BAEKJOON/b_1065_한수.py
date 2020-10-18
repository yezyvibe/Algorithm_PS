def hansoo(n):
    cnt = 99
    if n < 100:
        return n
    else:
        for i in range(100, n + 1):
            lst = list(str(i))
            if (int(lst[2]) - int(lst[1])) == (int(lst[1]) - int(lst[0])):
                cnt += 1
        else:
            return cnt

n = int(input())
print(hansoo(n))
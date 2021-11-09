arr = [1,2,3]
N = len(arr)

for i in range(1<<N):
    sub = []
    for j in range(N):
        if i & (1<<j):
            sub.append(arr[j])
    print(sub)
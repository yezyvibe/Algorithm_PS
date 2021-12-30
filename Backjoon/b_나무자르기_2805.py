import sys

def binary_search(height, trees):
    total = 0
    for tree in trees:
        if tree - height > 0:
            total += (tree - height)
    return total

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]

while start <= end:
    mid = (start + end) // 2
    res = binary_search(mid, trees)
    if  res >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
    


    

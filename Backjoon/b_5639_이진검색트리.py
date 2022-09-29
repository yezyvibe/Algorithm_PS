import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
# print(preorder)

def postorder(start, end):
    if start >= end:
        return

    mid = end
    for i in range(start+1, end):
        if preorder[start] < preorder[i]:
            mid = i
            break
    postorder(start+1, mid)
    postorder(mid, end)
    print(preorder[start]) # 루트 제일 마지막에 찍히도록

postorder(0, len(preorder))
# 고민하다가 잠이 오고,, 2시간 걸린,, 아이디어가 생각이 안났다!
# 높이가 같은 곳이 있으면 빗물이 고일 수 있다 -> 이때 높이가 최대인 것

h, w = map(int, input().split(' '))
blocks = list(map(int, input().split(' ')))

raindrop = 0
for i in range(len(blocks)):
    left, right = max(blocks[:i+1]), max(blocks[i:])
    low = min(left, right)
    raindrop += (low-blocks[i])
print(raindrop)
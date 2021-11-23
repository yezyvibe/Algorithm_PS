import sys
input = sys.stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())

while len(s) != len(t):
    if t[-1] == 'A':    # 문자열 S에 A를 추가할 수 있는 경우
        t.pop()
    else:               
        t.pop()
        t = t[::-1]
print(1 if t == s else 0)
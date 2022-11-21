import sys
import re

input = sys.stdin.readline
n = int(input())

pattern = input().replace('*', '[a-z]*')
p = re.compile(pattern)

for _ in range(n):
    filename = input()
    res = p.match(filename)
    
    if res == None:
        print("NE")
    else:
        print("DA")



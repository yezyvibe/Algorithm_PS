import sys

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
input = sys.stdin.readline
for i in range(10):
    a, b = map(int, input().rstrip().split(' '))
    for j in range((b-a+1)//2):
        num_list[a-1+j], num_list[b-j-1] = num_list[b-j-1], num_list[a-1+j]

print(' '.join(map(str, num_list)))
# import sys

# input = sys.stdin.readline
# n, k = map(int, input().split())
# answer = 0
# while bin(n).count('1') > k:
#     water = 2**(bin(n)[::-1].index('1'))
#     answer += water
#     n += water
# print(answer)


N,K=map(int,input().split())

def cheak(num):
    ans=0
    while(1):
        a=num//2
        b=num%2
        ans+=b
        num=a
        if num==0:
            break
    print(ans)
    return ans


if K>=N:
    print(0)
else:
    i = N
    while(1):
        print(i,'i')
        if cheak(i)<=K:
            print(i-N)
            break
        else:
            i+=1
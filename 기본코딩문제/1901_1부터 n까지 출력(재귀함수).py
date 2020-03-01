# n = int(input())
# def oneToN(n):
#   if(n!=1):
#     oneToN(n-1)
#   print(n)
# oneToN(n)

# n = int(input())
# def a(n):
#     if n != 1 :
#         a(n-1)
#     print(n)
# a(n)

n = int(input())
def a(cnt):
    if cnt == 0:
        return
    print(cnt)
    cnt -= 1
    a(cnt)
a(n)
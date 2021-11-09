# 점화식 이용해서 풀기
def combination(a , b):
    result=1
    for i in range(b):
        result*=(a-i)
    for j in range(1,b+1):
        result/=j
    return result
T=int(input())
for t in range(1,T+1):
    n=int(input())
    val=1
    ran=n//20
    n10=n//10
    for k in range(1,ran+1):
        val+=combination(n10-k,k)*(2**k)
    print('#{} {}'.format(t,int(val)))

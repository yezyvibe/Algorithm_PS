#메모이제이션 사용
import sys

def SuperSum(k, n):
    total=0
    if k == 0:
        total += n
        sum_lst[(k, n)] = n

    else:
        for i in range(1, n + 1):
            if (k - 1, i) not in sum_lst:
                sum_lst[(k-1, i)] = SuperSum(k - 1, i)
                total += sum_lst[(k-1,i)]
            else:
                total += sum_lst[(k - 1, i)]
    return total

for line in sys.stdin:
    k, n = map(int,line.split())
    total = 0
    sum_lst = {}

    print(SuperSum(k,n))
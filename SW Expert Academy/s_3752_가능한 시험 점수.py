T = int(input())
 
for test_case in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    val = 1
    for num in nums:
        val |= val << num
 
    print('#{} {}'.format(test_case, bin(val).count('1')))

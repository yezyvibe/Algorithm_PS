def solution(x):
    x_sum = [ int(i) for i in str(x) ]
    x_sum = sum(x_sum)
    if x % x_sum == 0:
        return True
    else:
        return False

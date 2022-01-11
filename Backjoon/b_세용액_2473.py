import sys 


def solution(N):
    input = sys.stdin.readline
    liquid = list(map(int, input().split()))
    liquid.sort()
    min_v = float("inf")
    answer = [0] * 3

    for i in range(N - 2):
        left, right = i + 1, N - 1

        while left != right:
            sum = liquid[i] + liquid[left] + liquid[right]

            if abs(sum) < abs(min_v):
                min_v = sum
                answer[0], answer[1], answer[2] = liquid[i], liquid[left], liquid[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            elif sum == 0:
                print(*answer)
                return
    print(*answer)

if __name__ == '__main__':
    solution(int(input()))
    
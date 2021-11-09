nums = input()

answer = 0
if '-' in nums: # 식에 - 연산자 있는 경우
    for i in range(len(nums)):
        if nums[i] == '-':
            f, b = nums[:i], nums[i + 1:]
            break
    for i in f.split('+'):
        answer += int(i)

    b = b.replace('-', '+').split('+')
    for i in b:
        answer -= int(i)

elif '+' in nums:  # 식에 + 연산자만 있는 경우
    for i in nums.split('+'):
        answer += int(i)

else:  # 연산자 없이 숫자 하나만 입력 받는 경우
    answer = nums
print(answer)

# 아래 잘못된 풀이
# nums = input()
#
# if '-' in nums:
#     nums = nums.split('-')
#     answer = int(nums[0])
#     for i in range(1, len(nums)):
#         n = nums[i]
#         if '+' in n:
#             n = n.split('+')
#             tmp = 0
#             for item in n:
#                 tmp += int(item)
#             answer -= tmp
#         else:
#             answer -= int(n)
# elif '+' in nums:
#     nums = nums.split('+')
#     answer = 0
#     for i in nums:
#         answer += int(i)
# else:
#     answer = int(nums)
# print(answer)

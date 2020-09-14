def solution(nums):
    answer = 0
    n_dic = {}
    for num in nums:
        print(num)
        if n_dic.get('num'):
            n_dic[num] += 1
        else:
            n_dic[num] = 1
    print(n_dic)
    # return answer
def solution(nums):
    answer = 0
    n_dic = {}
    for num in nums:
        if n_dic.get(num):
            n_dic[num] += 1
        else:
            n_dic[num] = 1

    pokemon = len(nums) // 2
    key_cnt = len(n_dic.keys())
    if pokemon >= key_cnt:
        return key_cnt
    else:
        return pokemon
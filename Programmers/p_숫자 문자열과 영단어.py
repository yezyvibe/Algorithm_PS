def solution(s):
    num_dic = {
        'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
        'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    result = ''
    num = ''
    for i in range(len(s)):
        tmp = s[i]
        if tmp.isdigit():
            result += tmp
        else:
            num += s[i]
            if num in num_dic:
                print(num)
                result += num_dic[num]
                num = ''   # num 초기화
    
    return int(result)
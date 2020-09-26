def lzw(w, dic, msg):
    idx = dic.index(w)
    if msg:
        dic.append(w+msg[0])
        
    return idx+1, dic

def solution(msg):
    answer = []
    dic = ['A']
    for i in range(1, 26):
        alp = chr(ord(dic[-1])+1)
        dic.append(alp)
        
    while msg:
        w = ''
        idx = 0
        for i in range(1, len(msg)+1):
            if msg[:i] in dic:
                w = msg[:i]
                idx = i
        msg = msg[idx:]
        tmp, dic = lzw(w, dic, msg)
        answer.append(tmp)
    
    return answer

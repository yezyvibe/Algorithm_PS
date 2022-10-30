from typing import List

def solution(k: int, dic: List[str], chat: str) -> str:
    chats = chat.split(" ")

    answer = []
    for i in range(len(chats)):
        cur_word = chats[i]
        # 같은 단어가 있는지 확인
        if cur_word in dic:
            answer.append("#"*len(cur_word))
            continue
    
        # 점을 바꿨을 때 같은 단어가 있는지 확인
        # 점이 중간에 있으면 앞 단어와 뒷 단어는 우선 고정이니 단어사전에서 비교
        
        dot_cnt = cur_word.count(".")
        if dot_cnt == 1:
            print(i)
            start, end = cur_word.split(".")
            word_len = len(cur_word)

            for j in range(len(dic)):
                compare = dic[j]
                if len(compare) < word_len:
                    continue
                print(compare[0:len(start)], compare[-len(end):])
                if compare[0:len(start)] == start and compare[-len(end):] == end:
                    answer.append("#"*len(compare))
                    print(answer)




k = 2
dic = ["slang", "badword"]
chat = "badword ab.cd bad.ord .word sl.. bad.word"
print(solution(k, dic, chat))
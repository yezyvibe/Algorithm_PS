from itertools import combinations as combi
def solution(orders, course):
    orders = list(map(list, orders))
    # print(orders)
    menu = list(set(sum(orders, [])))
    menu.sort()
    answer = []
    for i in course:
        menus = list(combi(menu, i))
        menu_len = i
        max_v = 1
        tmp = []
        for j in menus:
            idx = 0
            cnt = 0
            c_cnt = 0
            while idx < len(orders):

                for k in j:

                    if k in orders[idx]:
                        cnt += 1
                    else:
                        break
                else:
                    if cnt == menu_len:
                        c_cnt += 1


                if c_cnt > max_v:
                    tmp = [j]
                    max_v = c_cnt
                    # print(tmp, c_cnt, max_v,'ddddddddddddddddddddd')

                elif c_cnt == max_v:
                    if j not in tmp:
                        tmp.append(j)
                idx += 1
                cnt = 0
        if max_v > 1:
            answer.append(tmp)
            print(answer)
    answer = sum(answer, [])
    answer.sort()
    answer = [''.join(i) for i in answer]
    return answer


orders= ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
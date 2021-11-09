def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2,3단계
    id_list = []
    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            if id_list:
                if i ==  '.' and id_list[-1] == '.':
                    continue
            id_list.append(i)
            
    # 4단계
    if id_list:
        if id_list[0] == '.':
            id_list = id_list[1:]
    if id_list:
        if id_list[-1] == '.':
            id_list.pop()
    
    # 5단계
    if not id_list:
        id_list.append('a')

    # 6단계
    if len(id_list) >= 16:
        id_list = id_list[:15]
        if id_list[-1] == '.':
            id_list.pop()
    
    # 7단계
    if len(id_list) <= 2:
        last = id_list[-1]
        while len(id_list) != 3:
            id_list.append(last)
    
    return ''.join(id_list)

new_id = "=.="
print(solution(new_id))
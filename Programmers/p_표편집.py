def solution(n, k, cmd):
    deleted = []
    cur_idx = k
    linked = { i: [i-1, i+1] for i in range(n)}
    linked[0] = [None, 1]
    linked[n-1] = [n-2, None] 
    answer = ['O'] * n

    for i in range(len(cmd)):
        cur_cmd = cmd[i]
        
        if cur_cmd == 'C': # 삭제
            answer[cur_idx] = 'X'
            prev, next = linked[cur_idx]
            deleted.append([prev, cur_idx, next])

            if next == None:
                # 뒤가 없으면 앞으로 인덱스 이동
                cur_idx = linked[cur_idx][0]
            else:
                # 뒤 있으면 그대로 뒤로 이동
                cur_idx = linked[cur_idx][1]
            if prev == None:
                linked[next][0] = None
            elif next == None:
                linked[prev][1] = None
            else:
                linked[prev][1] = next
                linked[next][0] = prev

        elif cur_cmd == 'Z':
            prev, now, next = deleted.pop()
            answer[now] = 'O'
            if prev == None:
                linked[next][0] = now
            elif next == None:
                linked[prev][1] = now
            else:
                linked[prev][1] = now
                linked[next][0] = now

        else:
            command, cnt = cur_cmd.split(" ")
            cnt = int(cnt)
            if command == 'U':
                # 올라가기 
                for _ in range(cnt):
                    cur_idx = linked[cur_idx][0]
            
            elif command == 'D':
                # 내려가기
                for _ in range(cnt):
                    cur_idx = linked[cur_idx][1]
    return "".join(answer)
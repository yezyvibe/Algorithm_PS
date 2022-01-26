def impossible(result):
    COL, ROW = 0, 1  # COL 기둥, ROW 보
    for x, y, a in result:
        if a == COL: # 기둥일 때
            # 바닥이 아니거나 교차점의 아래가 기둥이 아니거나 교차점의 왼쪽이 보가 아니거나 교차점에 보가 없는 경우
            if y != 0 and (x, y-1, COL) not in result and \
                (x-1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else: # 보일 때
            # 양쪽 끝이 기둥이 아니거나 양쪽 끝에 보가 아닌 경우
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and \
        not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
    # 설치할 수 있는 경우 / 제거할 수 있는 경우
    return False

def solution(n, build_frame):
    result = set()
    
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            result.add(item)
            if impossible(result):
                # 추가 불가능한 경우
                result.remove(item)
        elif item in result: # 제거할 때
            result.remove(item)
            if impossible(result):
                # 제거 불가능한 경우
                result.add(item)
    answer = map(list, result)
    
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))
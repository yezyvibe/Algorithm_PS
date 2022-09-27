import sys
sys.setrecursionlimit(10**6)

def get_order(arr_x, arr_y, answer, order):
    node = arr_y[0] # 최상단 부모 노드
    idx = arr_x.index(node)
    arr_y_left, arr_y_right = [], []

    for i in range(1, len(arr_y)):
        if node[0] > arr_y[i][0]: # 왼쪽 위치
            arr_y_left.append(arr_y[i])
        else: # 오른쪽 위치
            arr_y_right.append(arr_y[i])
    if order == 'pre':
        answer.append(node[2])
    if len(arr_y_left) > 0:
        get_order(arr_x[:idx],arr_y_left, answer, order)
    if len(arr_y_right) > 0:
        get_order(arr_x[idx+1:],arr_y_right, answer, order)
    if order == 'post':
        answer.append(node[2])
    return


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
        
    arr_y = sorted(nodeinfo, key= lambda x:(-x[1], x[0]))
    arr_x = sorted(nodeinfo, key= lambda x:(x[0]))
    
    preanswer = []
    postanswer = []

    get_order(arr_x, arr_y, preanswer, 'pre')
    get_order(arr_x, arr_y, postanswer, 'post')
    
    return [preanswer, postanswer]




nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
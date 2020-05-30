from itertools import permutations as permu
from copy import deepcopy


def search(k, res):
    # 순열로 구한 각 집합에서 사탕을 하나씩 순차적으로 주었을 때,
    for a in range(n):
        if k[a] not in tmp_lst[a]: # 아이들이 가진 캔디 리스트에 해당 사탕이 없을 때만
            tmp_lst[a].append(k[a]) # 넣어주기

    # 사탕 배분이 다 끝난 뒤에, 각 아이들이 가진 캔디의 종류를 모두 센다
    for b in tmp_lst:
        res += len(b)
    # 종류의 수의 합을 리턴
    return res

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    child_candy = [[] for _ in range(n)] # 아이들이 가진 캔디 종류를 나타내는 리스트 (아래 if문을 통해 종류의 중복 없이 생성함)
    candy_lst = list(range(1, m+1)) # 전체 캔디의 종류를 나타내는 리스트
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in tmp[1::]:
            if j not in child_candy[i]:
                child_candy[i].append(j)

    if n > m: # 아이들의 수가 전체 캔디의 종류 보다 많은 경우를 처리하기 위해
        n = m # 순열을 올바르게 구하기 위한 조치 (아이의 수를 캔디 종류만큼으로 제한)
    candy_lst = list(permu(candy_lst, n))

    max_v = 0
    for k in candy_lst:
        tmp_lst = deepcopy(child_candy) # 아이들이 가진 캔디 종류를 보여준 원본 리스트가 바뀌는 것을 방지하기 위해 deepcopy 사용
        if search(k, 0) > max_v: # 종류의 수가 최대값인지 비교
            max_v = search(k, 0) # 최대값이면 max_v 갱신

    print('#{} {}'.format(tc, max_v))


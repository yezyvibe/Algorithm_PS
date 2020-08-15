def solution(numbers):
    # 아래는 주어진 숫자로 나타낼 수 있는 모든 숫자의 경우를 구하는 로직(중복불가)
    def dfs(word):
        if len(word) == k: # 문자길이가 k이면 결과 리스트에 넣기
            result.add(int(word))
            return

        for i in range(n):
            if visit[i] == 0:  # 방문하지 않았다면 word문자열에 붙이기
                visit[i] = 1
                dfs(word + numbers[i])
                visit[i] = 0  # 방문 리스트 복구

    result = set() # 중복을 없애기 위해서 set 자료형으로 설정
    numbers = list(numbers)
    n = len(numbers)
    visit = [0] * n
    for k in range(1, n + 1):
        dfs("")

    # 여기서부터 소수 찾는 로직
    answer = 0
    for i in result:
        if i == 1 or i == 0:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
            print(answer)
    return answer
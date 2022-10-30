# 종이배열? 접어서 최대 숫자 찾기

def solution(paper, n):
    answer = max(paper)

    def dfs(new_paper, n, cur_n):
        nonlocal answer
        answer = max(answer, max(new_paper))
        if n == cur_n:
            return

        for k in range(1, len(new_paper)):
            left, right = new_paper[:k], new_paper[k:]
            L_left, L_right = len(left), len(right)
            if L_left <= L_right:
                for i in range(L_left):
                    right[i] += left[-i-1]
                next_paper = right[:]
            else:
                for i in range(L_right):
                    left[-i -1] += right[i]
                next_paper = left[:]
            dfs(next_paper, n, cur_n + 1)

    dfs(paper, n, 0)
    return answer
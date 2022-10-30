def solution(today, terms, privacies):
    term_dic = {}
    
    def convertToDays(str):
        y, m, d = map(int, str.split("."))
        y = (y - 2000) * 12 * 28
        m = m * 28
        return y + m + d
        
    # 1일로 모두 통일하기
    n_today = convertToDays(today)
    
    for term in terms:
        alpha, months = term.split(" ")
        term_dic[alpha] = int(months) * 28

    answer = []
    for i in range(len(privacies)):
        start_date, alpha = privacies[i].split(" ")
        start_date = convertToDays(start_date)
        # 가능한 날짜
        if n_today > term_dic[alpha] + start_date - 1:
            answer.append(i+1)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
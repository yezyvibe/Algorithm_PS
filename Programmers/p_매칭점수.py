def search_word(sentence, word):
    sentence += ' '
    word = word.lower()
    sentence = sentence.lower()
    tmp = ''
    cnt = 0
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            tmp += sentence[i]
        else:
            # 알파벳 아닌 게 나오면 지금까지의 단어 비교하기
            if tmp == word:
                cnt += 1
            tmp = ''
    return cnt

def solution(word, pages):
    scores = [[0] * 2 for _ in range(len(pages))] # 기본점수, 링크점수 순서로 저장됨
    page_dict = {}
    for m in range(len(pages)):
        # 기본 점수 구하기 -> 검색어 등장 횟수
        # 링크 점수 구하기 -> 링크 걸린 다른 웹페이지의 기본점수 / 외부 링크 수
        # 기본 점수와 외부 링크 수를 먼저 찾아서 저장

        current = sum([ i.split('\t') for i in pages[m].split("\n")], [])
        body_start_idx = current.index('<body>') + 1
        body_end_idx = current.index('</body>')
        body = [i for i in current[body_start_idx:body_end_idx] if i]

        # 현재 페이지 url 알아내기
        url_idx = current.index('</head>  ') - 1
        while 'https://' not in current[url_idx] or 'meta' not in current[url_idx] or 'og:url' not in current[url_idx]:
            url_idx -= 1
        current_url = current[url_idx].split('https://')[-1][:-3].split('"')[0]
        if current_url not in page_dict:
            page_dict[current_url] = [m] # 외부 링크 저장하기 
        
        for k in range(len(body)):
            items = sum([i.split('<a href="') for i in body[k].split('</a>') if i ], [])
            for j in range(len(items)):
                if not items[j]:
                    continue
                elif items[j][:5] == 'https':
                    page_dict[current_url].append(items[j][:items[j].index(">")-1])
                else:
                    result = search_word(items[j], word) # 기본 점수 구해서 저장하기
                    scores[m][0] += result

    for key, val in page_dict.items():
        idx = val[0]
        for l in range(1, len(val)):
            link_score = 0
            url = val[l][8:]
            basic_score, total = scores[idx][0], len(val) - 1
            link_score += (basic_score / total)
            if url in page_dict:
                scores[page_dict[url][0]][1] += link_score

    answer = -1
    max_value = -1
    for i in range(len(scores)):
        total_score = sum(scores[i])
        if max_value < total_score:
            answer = i
            max_value = total_score
    return answer
word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n  <meta charset=\"utf-8\">\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))
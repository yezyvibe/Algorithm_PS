def solution(routes):
    routes.sort(key = lambda x:x[1])
    answer = 0
    visit = [0] * len(routes)
    camera = 0
    print(routes)
    for i in range(len(routes)):
        print(i, camera)
        if not visit[i]:
            visit[i] = 1
            camera = routes[i][1]
            answer += 1

            for j in range(i+1, len(routes)):
                if routes[j][0] <= camera <= routes[j][1] and not visit[j]:
                    visit[j] = 1
    return answer
                
        





# def solution(routes):
#     answer = 0
#     routes.sort(key = lambda x : x[1])
#     camera = -30001

#     for route in routes:
#         if camera < route[0]:
#             camera = route[1]
#             answer += 1

#     return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
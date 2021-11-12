microwave_button = [300, 60, 10]
cook_time = int(input())
if cook_time % 10:
    print(-1)
    exit(0)
idx = 0
answer = [0, 0, 0]
while cook_time != 0:
    if cook_time >= microwave_button[idx]:
        q, r = divmod(cook_time, microwave_button[idx])
        answer[idx] = q
        cook_time = r
    idx += 1
print(*answer)


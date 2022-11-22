import sys

input = sys.stdin.readline
N = int(input())

start_records = []
end_records = []

# 대근 기록
for _ in range(N):
    start_records.append(input().rstrip())

# 영식 기록
for _ in range(N):
    end_records.append(input().rstrip())

# print(start_records, end_records)


idx = 0
overtaked = set()
for i in range(N):
    current = start_records[i]

    if current in overtaked: # 이미 과속으로 단속된 경우
        continue

    while current != end_records[idx]:
        overtaked.add(end_records[idx])
        idx += 1

    idx += 1

print(len(overtaked))
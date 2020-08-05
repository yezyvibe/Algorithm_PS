# ["Enter uid1234 Muzi", 
# "Enter uid4567 Prodo",
# "Leave uid1234",
# "Enter uid1234 Prodo",
# "Change uid4567 Ryan"]
# 이름은 Enter, Change 할 때만 변경
# 최종 채팅방 메세지에 기록될 action은 Enter, Leave
# ['Enter', 'uid1234', 'Muzi']
# ['Enter', 'uid4567', 'Prodo']
# ['Leave', 'uid1234']
# ['Enter', 'uid1234', 'Prodo']
# ['Change', 'uid4567', 'Ryan']

name_list = {}
action_list = []
result = []

for record in records:
	record = record.split(' ')
	action = record[0]
	print(record)

	# 새로 생성 하거나 이름 변경하기
	if  action == "Enter" or  action == "Change":
		name_list[record[1]] = record[2] #key는 id, value는 닉네임
	# 들어오거나 나갈 때를 기록하기
	if action == "Enter" or  action == "Leave":
		action_list.append((record[1] ,record[0])) # id, 행동

for id, action in action_list:
	if action == "Enter":
		result.append(name_list[id] + "님이 들어왔습니다.")
	else:
		result.append(name_list[id] + "님이 나갔습니다.")
		
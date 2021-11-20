import sys
def if_boy(num, switch_state):
    for i in range(1, len(switch_state)+1):
        if i % num == 0:
            if switch_state[i-1]:
                switch_state[i-1] = 0
            else:
                switch_state[i-1] = 1

def if_girl(num, switch_state):
    front = num-2
    back = num
    if switch_state[num-1]:
        switch_state[num-1] = 0
    else:
        switch_state[num-1] = 1
    while front >= 0 and back < len(switch_state):
        if switch_state[front] == switch_state[back]:
            if switch_state[front]:
                switch_state[front] = 0
                switch_state[back] = 0
            else:
                switch_state[front] = 1
                switch_state[back] = 1
            front -= 1
            back += 1
        else:
            break


input = sys.stdin.readline
switch = input()
switch_state = list(map(int, input().rstrip().split(' ')))
student = int(input())
for i in range(student):
    s, num = map(int, input().rstrip().split(' '))
    if s == 1:
        if_boy(num, switch_state)
    else:
        if_girl(num, switch_state)
        
if len(switch_state) > 20:
    answer = [switch_state[i:i+20] for i in range(0, len(switch_state), 20)]
    for i in answer:
        print(' '.join(map(str, i)))
else:       
    print(' '.join(map(str, switch_state)))
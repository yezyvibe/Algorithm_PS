def add_letter_a(word):
    if word[-1] == 'A':
        word.pop()
        return word

def add_letter_b_and_reverse(word):
    if word[0] == 'B':
        word = word[::-1]
        word.pop()
        return word
    

s = list(input())
t = list(input())
answer = False
def check(a):
    global answer
    if len(a) == len(s):
        if a == s:
            answer = True
        return False
    
    if a[0] == 'B':
        a = a[::-1]
        a.pop()
        check(a)
        a.append('B')  # a를 원상복구
        a = a[::-1] 
    if a[-1]  == 'A':
        a.pop()
        check(a)
        a.append('A')  # a를 원상복구

check(t)
if answer:
    print(1)
else:
    print(0)
    
        

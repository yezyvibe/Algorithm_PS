variable = input().split(' ')
start = variable[0]
for i in range(1, len(variable)):
    tmp = start
    tmp_alpha = ''
    for j in range(len(variable[i])-1, -1, -1):
        if variable[i][j] == ',':
            continue
        elif variable[i][j] == '[':
            tmp += '[]'
        elif variable[i][j] in ['&', '*']:
            tmp += variable[i][j]
        elif variable[i][j].isalpha():
            tmp_alpha += variable[i][j]
    
    tmp += ' '
    tmp += tmp_alpha[::-1]        
    tmp += ';'
    print(tmp)
n = int(input())
s_list = []

def w(n, s_list):
    if n == 1:
        s_list.append(n)
        s_list.reverse()
        print('\n'.join(map(str, s_list)))
        return
    elif n % 2 == 1:
        s_list.append(n)
        n = 3*n+1
        w(n, s_list)
    else:
        s_list.append(n)
        n = n // 2
        w(n, s_list)

    # res = s_list.reverse()
    # print(res)
    # return
w(n,s_list)
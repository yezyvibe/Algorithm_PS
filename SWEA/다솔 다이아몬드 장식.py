T = int(input())
for tc in range(1,T+1):
    letters = input()

    a,b,c = '','',''


    for i in range(len(letters)):
        a += '..#.'
        b += '.#.#'
        c += '#.'+letters[i]+'.'

    a +='.'
    b +='.'
    c +='#'

    print(a,b,c,,e,sep = '\n')


T = int(input())
for tc in range(1, T + 1):
    letters = input()

    a = ''
    b = ''
    c = ''
    d = ''
    e = ''

    for i in range(len(letters)):
        a += '..#.'
        b += '.#.#'
        c += '#.' + letters[i] + '.'
        d += '.#.#'
        e += '..#.'

    a += '.'
    b += '.'
    c += '#'
    d += '.'
    e += '.'

    print(a, b, c, d, e, sep='\n')

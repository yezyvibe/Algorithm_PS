dic = {
    'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
    'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)
}

char_list = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

char_str = 'ABCDEFGH'

k, s, n = input().split(' ')
ky, kx = char_list[k[0]], abs(int(k[1]) - 8)
sy, sx = char_list[s[0]], abs(int(s[1]) - 8)

for _ in range(int(n)):
    t = input()
    dx, dy = dic[t][0], dic[t][1]
    nx, ny = kx + dx, ky + dy

    if 0 <= nx < 8 and 0 <= ny < 8:
        kx, ky = nx, ny
        if kx == sx and ky == sy:
            if 0 <= sx + dx < 8 and 0 <= sy + dy < 8:
                sx += dx
                sy += dy
            else:
                kx -= dx
                ky -= dy

print(char_str[ky] + str(abs(kx - 8)))
print(char_str[sy] + str(abs(sx - 8)))

def solution(files):
    changed = []
    idx = 0
    for file in files:
        head = ''
        number = ''
        tail = ''
        chk = 0
        for i in file:
            if i.isdigit() and len(number) < 5:
                number += str(i)
                chk = 1
            elif not chk:
                head += i.upper()
            else:
                break
        changed.append([head, int(number), idx,  file])
        idx += 1
    changed.sort()
    return [changed[i][3] for i in range(len(files))]
files = ["abc123456", "abc123455", "img02.png", "img1.png", "IMG01.GIF", "img2"]
print(solution(files))

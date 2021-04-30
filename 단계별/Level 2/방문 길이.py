from collections import defaultdict


def solution(dirs):
    checked = defaultdict(list)
    x, y = 0, 0
    answer = 0
    for d in dirs:
        if d == 'U':
            nx = x + 1
            ny = y
        elif d == 'D':
            nx = x - 1
            ny = y
        elif d == 'R':
            nx = x
            ny = y + 1
        else:
            nx = x
            ny = y - 1

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (nx, ny) not in checked[(x, y)]:
                answer += 1
                checked[(x, y)].append((nx, ny))
                checked[(nx, ny)].append((x, y))
            x, y = nx, ny

    return answer
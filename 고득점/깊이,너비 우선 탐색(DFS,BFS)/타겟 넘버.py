from collections import deque

# bfs
def solution(numbers, target):
    qu = deque()
    qu.append([numbers[0], 1])
    qu.append([-numbers[0], 1])

    cnt = 0
    while qu:
        num, idx = qu.pop()
        if num == target and idx == len(numbers):
            cnt += 1
        elif idx < len(numbers):
            qu.append([num + numbers[idx], idx + 1])
            qu.append([num - numbers[idx], idx + 1])

    return cnt

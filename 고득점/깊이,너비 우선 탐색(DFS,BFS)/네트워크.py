from collections import deque


def solution(n, computers):
    def dfs(i):
        qu = deque()
        qu.append(i)
        while qu:
            v = qu.pop()
            computers[v][v] = -1
            for j in range(n):
                if computers[v][j] == 1:
                    qu.append(j)
                    computers[v][j] = -1

    cnt = 0
    for i in range(n):
        if 1 in computers[i]:
            dfs(i)
            cnt += 1

    return cnt
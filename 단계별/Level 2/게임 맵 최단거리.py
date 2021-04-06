from collections import deque

def solution(maps):
    def bfs(i, j):
        qu = deque()
        qu.append((i, j))
        visited[i][j] = 1

        while qu:
            x, y = qu.popleft()
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny]:  # 이동가능한 범위
                    if not visited[nx][ny]:
                        if nx == N - 1 and ny == M - 1:
                            return visited[x][y] + 1

                        qu.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1

        return -1

    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = bfs(0, 0)

    return result
def solution(n):
    arr = [[0] * (i + 1) for i in range(n)]
    dir = [(1, 0), (0, 1), (-1, -1)]

    # 달팽이 채우기
    x, y = 0, 0
    cnt = 1
    arr[0][0] = cnt
    total = (n + 1) / 2 * n
    while cnt < total:
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            while 0 <= nx < n and 0 <= ny < nx + 1 and not arr[nx][ny]:
                cnt += 1
                arr[nx][ny] = cnt

                nx += d[0]
                ny += d[1]
            x = nx - d[0]
            y = ny - d[1]

    answer = []
    for a in arr:
        answer += a
    return answer
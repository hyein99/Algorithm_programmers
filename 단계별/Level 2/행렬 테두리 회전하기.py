def solution(rows, columns, queries):
    # arr 입력
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1

    answer = []
    for x1, y1, x2, y2 in queries:
        x, y = x1 - 1, y1 - 1
        tmp = arr[x + 1][y]
        minN = tmp
        while y != y2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += 1
        while x != x2 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += 1
        while y != y1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            y += -1
        while x != x1 - 1:
            arr[x][y], tmp = tmp, arr[x][y]
            minN = min(minN, tmp)
            x += -1

        answer.append(minN)

    return answer
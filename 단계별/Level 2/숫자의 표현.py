def solution(n):
    cnt = 1  # 자기자신은 무조건 포함

    # start: 연속하는 수 중 가장 큰수
    for start in range(n - 2, 1, -1):
        cont_sum = 0
        addnum = start
        while cont_sum < n:
            cont_sum += addnum
            addnum -= 1
            if addnum < 1:
                break

        if cont_sum == n:
            cnt += 1

    return cnt
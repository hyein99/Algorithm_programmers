def solution(x, n):
    answer = []
    tmp = x
    for _ in range(n):
        answer.append(tmp)
        tmp += x
    return answer
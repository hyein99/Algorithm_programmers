def solution(n):
    answer = -1
    x = 1
    while x*x <= n:
        if x*x == n:
            answer = (x+1)*(x+1)
        x += 1
    return answer
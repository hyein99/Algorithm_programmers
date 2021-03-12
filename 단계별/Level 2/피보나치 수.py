def solution(n):
    x, y = 0, 1
    for i in range(1, n+1):
        x, y = y, (x+y)%1234567
    return x
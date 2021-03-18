def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            x = '4'
        elif n % 3 == 1:
            x = '1'
        else:
            x = '2'
        answer = x + answer
        n = (n - 1) // 3
    return answer



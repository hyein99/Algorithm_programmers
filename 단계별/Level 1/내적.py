def solution(a, b):
    answer = [x*y for x, y, in zip(a, b)]
    return sum(answer)
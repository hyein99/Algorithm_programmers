def solution(arr, divisor):
    answer = sorted([a for a in arr if a%divisor==0])
    if not answer:
        answer = [-1]
    return answer
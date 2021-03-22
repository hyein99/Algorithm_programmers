def solution(w, h):
    # step 1. 전체 정사각형 개수
    answer = w * h

    # step 2. 잘리는 정사각형 개수
    # gcd(w,h) 구하기
    n = 2
    gcd = 1
    while n <= min(w, h):
        if w % n == 0 and h % n == 0:
            gcd *= n
            w //= n
            h //= n
        else:
            n += 1
    exclude = gcd * (w + h - 1)
    return answer - exclude
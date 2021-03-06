def solution(numbers, hand):
    answer = ''
    lloc = [3, 0]
    rloc = [3, 2]
    H = 'R' if hand == 'right' else 'L'

    for n in numbers:
        if n % 3 == 0 and n:
            h = 'R'
            rloc = [n // 3 - 1, 2]
        elif n % 3 == 1:
            h = 'L'
            lloc = [n // 3, 0]
        else:  # 2,5,8,0
            if n == 0:
                loc = [3, 1]
            else:
                loc = [n // 3, 1]
            ldist = abs(loc[0] - lloc[0]) + abs(loc[1] - lloc[1])
            rdist = abs(loc[0] - rloc[0]) + abs(loc[1] - rloc[1])
            if ldist < rdist:
                h = 'L'
            elif ldist > rdist:
                h = 'R'
            else:
                h = H
            if h == 'R':
                rloc = loc
            else:
                lloc = loc

        answer += h

    return answer
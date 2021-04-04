def solution(n, t, m, p):
    def baseN(N):
        if N == 0:
            return '0'
        result = ''
        while N:
            result = str(nlist[N % n]) + result
            N //= n
        return result

    # step 1: n진법
    nlist = [i for i in range(0, 10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    nlist = nlist[:n]

    # step 2: n진법으로 nstr의 길이가 t*m이 될때까지 구함
    nstr = ''
    i = 0
    while len(nstr) <= t * m:
        nstr += baseN(i)
        i += 1

    # step 3: p번째 순서일때 result
    answer = ''
    i = p - 1
    while len(answer) < t:
        answer += nstr[i]
        i += m

    return answer
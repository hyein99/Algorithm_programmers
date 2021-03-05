def solution(n):
    j = 2
    expt = set()
    while j*2 <= n:
        k = 2
        while j*k <= n:
            expt.add(j*k)
            k += 1
        j += 1
    return n-1-len(expt)
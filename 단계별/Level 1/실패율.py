def solution(N, stages):
    slist = [0 for _ in range(N + 1)]
    for n in stages:
        for i in range(n):
            slist[i] += 1
    frate = [[i, 0] for i in range(1, len(slist))]
    for j in range(1, len(slist)):
        if slist[j - 1] == 0:
            break
        frate[j - 1][1] = (slist[j - 1] - slist[j]) / slist[j - 1]
    frate.sort(key=lambda x: (-x[1], x[0]))

    return [x[0] for x in frate]

def solution(s):
    minlen = len(s)
    for i in range(1, len(s) // 2 + 1):
        orgs = s
        news = ''
        while len(orgs) >= 2 * i:
            cnt = 1
            while orgs[:i] == orgs[i:2 * i]:
                cnt += 1
                reps = orgs[:i]
                orgs = orgs[i:]
            if cnt > 1:
                news += str(cnt) + reps
                orgs = orgs[i:]
            else:
                news += orgs[:i]
                orgs = orgs[i:]
        news += orgs
        minlen = min(minlen, len(news))

    return minlen

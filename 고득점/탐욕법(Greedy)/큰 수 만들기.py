def solution(number, k):
    nlist = list(number)
    if len(nlist) <= 2:
        return str(max(nlist))
    cnt = 0
    i = 1
    while cnt < k:
        if i >= len(nlist):
            nlist.pop(i - 1)
            break
        if int(nlist[i - 1]) < int(nlist[i]):
            nlist.pop(i - 1)
            i -= 1 if i > 1 else 0
            cnt += 1
        else:
            i += 1

    return ''.join(nlist)

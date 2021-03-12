def solution(s):
    slist = list(map(int, s.split()))
    slist.sort()
    return str(slist[0])+' '+str(slist[-1])
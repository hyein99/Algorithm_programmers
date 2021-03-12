def solution(s):
    cnt = 0
    flag = True
    for p in s:
        if p == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                flag = False
                break
    if cnt==0 and flag:
        return True
    else:
        return False
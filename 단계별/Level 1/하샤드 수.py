def solution(x):
    xsum = 0
    tmp = x
    while tmp > 0:
        xsum += tmp%10
        tmp = (tmp-tmp%10)/10
    if x%xsum:
        return False
    else:
        return True
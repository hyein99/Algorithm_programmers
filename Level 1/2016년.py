def solution(a, b):
    dsum = b
    a -= 1
    while a:
        if a in [1,3,5,7,8,10,12]:
            dsum += 31
        elif a==2:
            dsum += 29
        else:
            dsum += 30
        a -= 1

    if dsum%7==1:
        answer = 'FRI'
    elif dsum%7==2:
        answer = 'SAT'
    elif dsum%7==3:
        answer = 'SUN'
    elif dsum%7==4:
        answer = 'MON'
    elif dsum%7==5:
        answer = 'TUE'
    elif dsum%7==6:
        answer = 'WED'
    else:
        answer = 'THU'
    return answer
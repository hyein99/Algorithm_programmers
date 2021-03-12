import math

def solution(progresses, speeds):
    answer = []
    i = 0
    time = 0
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        if time == 0:
            cnt = 1
            time = math.ceil((100-p)/s)
        elif math.ceil((100-p)/s) <= time:
            cnt += 1
        else:
            answer.append(cnt)
            time = math.ceil((100-p)/s)
            cnt = 1
    answer.append(cnt)
    return answer
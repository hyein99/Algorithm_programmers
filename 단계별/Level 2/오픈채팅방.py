from collections import defaultdict


def solution(record):
    answer = []
    names = defaultdict()
    for i in range(len(record)):
        rlst = record[i].split()
        if rlst[0] == 'Leave':
            answer.append(rlst[1] + '님이 나갔습니다.')
        elif rlst[0] == 'Enter':
            answer.append(rlst[1] + '님이 들어왔습니다.')
            names[rlst[1]] = rlst[2]
        else:
            names[rlst[1]] = rlst[2]

    for i in range(len(answer)):
        uid = answer[i].split('님')[0]
        answer[i] = answer[i].replace(uid, names[uid])

    return answer
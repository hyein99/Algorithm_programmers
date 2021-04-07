# 풀이 1) 해시 사용
from collections import defaultdict

def solution(participant, completion):
    cdict = defaultdict(int)
    for c in completion:
        cdict[c] += 1

    for p in participant:
        if cdict[p]:
            cdict[p] -= 1
        else:
            return p

# 풀이 2) 정렬 사용
# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
#
#     for i in range(0, len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break
#     if answer == '':
#         answer = participant[-1]
#     return answer
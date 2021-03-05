def solution(n):
    answer = 0
    tnum = []
    while n>0:
        tnum.append(n%3)
        n //= 3
    print(tnum)
    for i in range(len(tnum)):
        answer += tnum[len(tnum)-1-i]*(3**i)
    return answer

print(solution(45))

# 45/3=15 ...0
# 15/3=5  ...0
# 5/3=1   ...2
# 1/3=0   ...1
# 1200 > 0021
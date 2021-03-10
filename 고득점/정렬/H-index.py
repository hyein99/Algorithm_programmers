def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] > h:
            h += 1
    return h

print(solution(citations=[5]))
print(solution(citations=[10, 8, 5, 4, 3]))
print(solution(citations=[25, 8, 5, 3, 3]))
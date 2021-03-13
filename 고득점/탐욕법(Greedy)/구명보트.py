def solution(people, limit):
    i, j = 0, len(people) - 1
    people.sort()
    cnt = 0
    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        elif i == j:
            break
        else:
            j -= 1

    return cnt
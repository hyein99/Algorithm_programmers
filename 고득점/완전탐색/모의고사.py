def solution(answers):
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == st1[i % 5]:
            cnt1 += 1
        if answers[i] == st2[i % 8]:
            cnt2 += 1
        if answers[i] == st3[i % 10]:
            cnt3 += 1
    maxcnt = max(cnt1, cnt2, cnt3)

    answer = []
    if maxcnt == cnt1:
        answer.append(1)
    if maxcnt == cnt2:
        answer.append(2)
    if maxcnt == cnt3:
        answer.append(3)

    return answer
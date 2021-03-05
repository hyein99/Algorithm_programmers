def solution(s):
    slist = s.split(' ')
    answer = ''
    for s in slist:
        for i in range(len(s)):
            if i%2:
                answer += s[i].lower()
            else:
                answer += s[i].upper()
        answer += ' '
    return answer[:-1]
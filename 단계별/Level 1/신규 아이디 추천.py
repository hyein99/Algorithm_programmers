def solution(new_id):
    # 1, 2단계
    answer = ''
    for s in new_id:
        if s.isalpha():
            answer += s.lower()
        elif s in '-_.' or s.isdigit():
            answer += s

    # 3, 4단계
    answer = '.'.join(answer.replace('.', ' ').split())
    print(answer)
    # 5,6,7단계
    if not answer:
        answer = 'aaa'
    elif len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    elif len(answer) > 15:
        answer = answer[:14] if answer[14] == '.' else answer[:15]

    return answer
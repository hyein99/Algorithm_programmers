def check_str(str):
    s = []
    for c in str:
        if c in '{[(':
            s.append(c)
        else:
            if not s:
                return False
            if c == '}':
                x = s.pop()
                if x != '{':
                    return False
            elif c == ']':
                x = s.pop()
                if x != '[':
                    return False
            else:
                x = s.pop()
                if x != '(':
                    return False
    if s:
        return False
    return True


def solution(s):
    answer = 0
    i = 0
    while i < len(s):
        # 올바른 문자열 판별
        if check_str(s):
            answer += 1
            i += 2
            s = s[2:] + s[:2]
        else:
            i += 1
            s = s[1:] + s[:1]

    return answer
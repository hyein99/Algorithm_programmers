def solution(name):
    def move_joy(x):
        return min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)

    result = 0
    # 첫번째 글자
    result += move_joy(name[0])
    if len(name) < 2:
        return result

    # 건너 뛸 A
    i = 1
    while name[i] == 'A':
        i += 1

    while i < len(name):
        result += move_joy(name[i]) + 1
        i += 1

    return result

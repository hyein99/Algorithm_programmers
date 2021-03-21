def choosedir(idx, dlist):
    right, left = 1, 1
    while dlist[idx + right] == 0:
        right += 1
    while dlist[idx - left] == 0:
        # print(idx-left)
        left += 1

    if left < right:
        move = left
        new_idx = idx - move
    else:
        move = right
        new_idx = idx + move

    return new_idx, move


def solution(name):
    answer = 0
    # step 1: name[i]를 A로 바꾸기 위한 최소 이동거리
    dlist = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]

    # step 2
    idx = 0
    cnt = len(dlist) - dlist.count(0)  # 바꿔야할 문자수

    while True:
        answer += dlist[idx]  # 바꿈
        if dlist[idx] != 0:
            cnt -= 1
        dlist[idx] = 0  # 이동 완료

        # 종료 조건
        if cnt <= 0:
            break

        # 오? 왼?
        idx, move = choosedir(idx, dlist)  # 이동한 위치, 오 왼 이동 거리 반환
        answer += move

    return answer


# JBAAAAAC


# def solution(name):
#     def move_joy(x):
#         return min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)
#
#     result = 0
#     # 첫번째 글자
#     result += move_joy(name[0])
#     if len(name) < 2:
#         return result
#
#     # 건너 뛸 A
#     i = 1
#     while name[i] == 'A':
#         i += 1
#
#     while i < len(name):
#         result += move_joy(name[i]) + 1
#         i += 1
#
#     return result


print(solution('JAM'))
print(solution('ABAAAAAAAAABB'))

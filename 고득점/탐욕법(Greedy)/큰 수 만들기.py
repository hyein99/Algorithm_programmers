# 문자열을 이용한 그리디
def solution(number, k):
    if len(number) == 2:
        return str(max(number[0], number[1]))

    cnt = 0  # 제거한 수
    idx = 1  # number의 index
    while cnt < k:
        if idx >= len(number):
            number = number[:idx - 1]
            break

        if int(number[idx - 1]) < int(number[idx]):
            number = number[:idx - 1] + number[idx:]
            idx -= 1 if idx > 1 else 0
            cnt += 1
        else:
            idx += 1

    return number

# 리스트를 사용한 그리디 >> 시간초과
# def solution(number, k):
#     nlist = list(number)
#     if len(nlist) <= 2:
#         return str(max(nlist))
#
#     cnt = 0
#     idx = 1
#     while cnt < k:
#         if idx >= len(nlist):
#             nlist.pop(idx - 1)
#             break
#         if int(nlist[idx - 1]) < int(nlist[idx]):
#             nlist.pop(idx - 1)
#             idx -= 1 if idx > 1 else 0
#             cnt += 1
#         else:
#             idx += 1
#
#     return ''.join(nlist)


# 순열 >> 시간초과
# def solution(number, k):
#     def make_biggest_num(s, idx, max_num):
#         if len(s) == len(number) - k:
#             max_num = max(max_num, int(s))
#             return max_num
#
#         for i in range(idx, len(number)):
#             max_num = make_biggest_num(s + number[i], i + 1, max_num)
#
#         return max_num
#
#     return str(make_biggest_num('', 0, 0))

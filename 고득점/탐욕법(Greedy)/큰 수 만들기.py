def solution(number, k):
    nlist = list(number)
    if len(nlist) <= 2:
        return str(max(nlist))
    cnt = 0
    i = 1
    while cnt < k:
        if i >= len(nlist):
            nlist.pop(i - 1)
            break
        if int(nlist[i - 1]) < int(nlist[i]):
            nlist.pop(i - 1)
            i -= 1 if i > 1 else 0
            cnt += 1
        else:
            i += 1

    return ''.join(nlist)



# 시간초과
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

def split_str(s):
    str_list = []
    sub_s = ''
    for i in range(len(s)):
        sub_s += s[i]
        if len(sub_s) == 2:
            if sub_s.isalpha():
                str_list.append(sub_s.lower())
            sub_s = sub_s[1]

    return str_list


def solution(str1, str2):
    # 다중집합 만들기
    str1_list = sorted(split_str(str1))
    str2_list = sorted(split_str(str2))

    if not str1_list and not str2_list:
        return 65536

    # 유사도 계산
    intersection = 0
    union = 0
    i, j = 0, 0

    while i < len(str1_list) and j < len(str2_list):
        if str1_list[i] == str2_list[j]:
            i += 1
            j += 1
            intersection += 1
            union += 1
        elif str1_list[i] > str2_list[j]:
            j += 1
            union += 1
        else:
            i += 1
            union += 1
    union += (len(str1_list) - i) + (len(str2_list) - j)

    answer = int(intersection / union * 65536)
    return answer
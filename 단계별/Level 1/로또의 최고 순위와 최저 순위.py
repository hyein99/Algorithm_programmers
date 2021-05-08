def solution(lottos, win_nums):
    # 정렬
    lottos.sort()
    win_nums.sort()

    min_num = 0
    max_num = 0
    i, j = 0, 0
    while i < 6 and j < 6:
        if lottos[i] == 0:
            max_num += 1
            i += 1
            continue
        elif lottos[i] < win_nums[j]:
            i += 1
        elif lottos[i] > win_nums[j]:
            j += 1
        else:
            min_num += 1
            max_num += 1
            i += 1
            j += 1

    if max_num < 2:
        max_num = 1
    if min_num < 2:
        min_num = 1

    answer = [7 - max_num, 7 - min_num]
    # 당첨 가능한 최고 순위와 최저 순위 return
    return answer
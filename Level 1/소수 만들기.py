def solution(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                nsum = nums[i] + nums[j] + nums[k]
                # 소수 판별
                flag = True
                for l in range(2, nsum):
                    if nsum % l == 0:
                        flag = False
                        break
                if flag:
                    cnt += 1

    return cnt
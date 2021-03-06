def solution(nums):
    answer = set(nums)
    if len(answer) > len(nums)/2:
        return len(nums)/2
    else:
        return len(answer)
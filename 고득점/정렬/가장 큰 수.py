# Solution 1. 삽입정렬 > 시간초과
# def solution(numbers):
#     def swap(x, y):
#         return int(str(x) + str(y)) < int(str(y) + str(x))
#
#     # 삽입정렬
#     for i in range(1, len(numbers)):
#         key = numbers[i]
#         j = i - 1
#         while j >= 0 and swap(numbers[j], key):
#             numbers[j + 1] = numbers[j]
#             j -= 1
#         numbers[j + 1] = key
#
#     return ''.join(str(n) for n in numbers)

def solution(numbers):
    def swap(x, y):
        return int(str(x) + str(y)) < int(str(y) + str(x))

    # 삽입정렬
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and swap(numbers[j], key):
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    return ''.join(str(n) for n in numbers)
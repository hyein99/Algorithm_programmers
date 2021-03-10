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

# Solution 2. 병합정렬
def solution(numbers):
    def swap(x, y):
        return int(str(x) + str(y)) < int(str(y) + str(x))

    # 병합정렬
    def merge_sort(arr):
        if len(arr) <= 1:
            return
        g1 = arr[:len(arr)//2]
        g2 = arr[len(arr)//2:]
        merge_sort(g1)
        merge_sort(g2)

        i1, i2, ia = 0, 0, 0
        while i1 < len(g1) and i2 < len(g2):
            if swap(g1[i1], g2[i2]):
                arr[ia] = g2[i2]
                ia += 1
                i2 += 1
            else:
                arr[ia] = g1[i1]
                ia += 1
                i1 += 1
        while i1 < len(g1):
            arr[ia] = g1[i1]
            ia += 1
            i1 += 1
        while i2 < len(g2):
            arr[ia] = g2[i2]
            ia += 1
            i2 += 1

    merge_sort(numbers)
    return str(int(''.join(map(str, numbers))))

print(solution(numbers=[0, 0]))
print(solution(numbers=[6, 10, 2]))
print(solution(numbers=[3, 30, 34, 5, 9]))
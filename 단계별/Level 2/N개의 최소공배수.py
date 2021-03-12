def solution(arr):
    num = max(arr)
    result = 1
    i = 2
    while i <= num + 1:
        print(i, arr, result)
        flag = True
        for j in range(len(arr)):
            if arr[j] % i == 0:
                flag = False
                arr[j] //= i
        if flag:  # 약수 아님
            i += 1
        else:
            result *= i

    return result

print(solution(arr=[3, 4, 9, 16])) #144
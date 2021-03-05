def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            print(arr1[i], arr2[i])
            if arr1[i] < 2 ** (n - j - 1) and arr2[i] < 2 ** (n - j - 1):
                tmp += ' '
            else:
                if arr1[i] >= 2 ** (n - j - 1):
                    arr1[i] -= 2 ** (n - j - 1)
                if arr2[i] >= 2 ** (n - j - 1):
                    arr2[i] -= 2 ** (n - j - 1)
                tmp += '#'
        answer.append(tmp)

    return answer

print(solution(n=5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]))
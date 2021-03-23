def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        row = arr1[i]
        for j in range(len(arr2[0])):
            col = [a[j] for a in arr2]
            tmp.append(sum([r*c for r, c in zip(row, col)]))
        answer.append(tmp)
    return answer
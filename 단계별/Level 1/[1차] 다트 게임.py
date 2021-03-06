def solution(dartResult):
    n = 0

    answer = 0
    while dartResult:
        # 점수
        i = 1
        if dartResult[1].isdigit():
            num = int(dartResult[:2])
            i += 1
        else:
            num = int(dartResult[0])
        # 보너스
        if dartResult[i] == 'S':
            nxtn = num
        elif dartResult[i] == 'D':
            nxtn = num ** 2
        else:
            nxtn = num ** 3
        i += 1

        if len(dartResult) < i+1:
            opt = ''
            dartResult = ''
        else:
            if dartResult[i].isdigit():
                opt = ''
                dartResult = dartResult[i:]
            else:
                opt = dartResult[i]
                dartResult = dartResult[i+1:]
        if opt == '#':
            nxtn *= -1
        elif opt == '*':
            n *= 2
            nxtn *= 2

        answer += n
        n = nxtn

    return answer + n

print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
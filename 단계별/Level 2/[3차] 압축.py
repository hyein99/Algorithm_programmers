def solution(msg):
    # msg = 'KAKAO'
    alpha_dict = dict()
    for i in range(26):
        alpha_dict[chr(i + 65)] = i + 1

    result = []
    i = 0
    cnt = 27
    while i < len(msg):
        m = msg[i]
        while m in alpha_dict:
            i += 1
            if i >= len(msg):
                break
            m += msg[i]

        if i < len(msg):
            result.append(alpha_dict[m[:-1]])
            alpha_dict[m] = cnt
            cnt += 1
        else:
            result.append(alpha_dict[m])

    return result
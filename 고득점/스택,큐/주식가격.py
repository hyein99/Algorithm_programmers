def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break

        answer.append(cnt)
    return answer

# prices[0 ] = 498 값은 prices[2] = 470 으로 감소하는데 2초가 걸렸다.
# prices[1] = 501 값은 prices[2] = 470 으로 감소하는데 1초가 걸렸다.
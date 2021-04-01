def solution(land):
    answer = land[0]
    for i in range(1, len(land)):
        next_answer = []
        for j in range(4):
            next_ground = 0
            for k in range(4):
                if j != k:
                    next_ground = max(next_ground, answer[k])
            next_answer.append(land[i][j] + next_ground)
        answer = next_answer
    return max(answer)
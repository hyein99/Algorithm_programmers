def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(box)>=2:
            if box[-1]==box[-2]:
                box = box[:-2]
                answer += 2
    #print(box)

    return answer
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new = array[commands[i][0] - 1: commands[i][1]]
        new.sort()
        answer.append(new[commands[i][2] - 1])
    return answer
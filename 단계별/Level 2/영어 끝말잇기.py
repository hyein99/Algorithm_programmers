def solution(n, words):
    round = 1
    prev_word = ''
    word_set = set()
    for i in range(0, len(words), n):
        for j in range(n):
            if len(words[i+j]) < 2 or (prev_word and prev_word[-1] != words[i+j][0]) or words[i+j] in word_set:
                return [j+1, round]
            prev_word = words[i+j]
            word_set.add(words[i+j])
        round += 1
    return [0,0]
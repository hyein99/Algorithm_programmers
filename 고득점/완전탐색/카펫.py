import math


def solution(brown, yellow):
    box = brown + yellow
    for i in range(1, int(math.sqrt(box)) + 1):  # 카펫 크기
        if box % i == 0:  # 카펫 세로 길이 가능
            h = i
            w = box // i

            for j in range(1, h - 1):  # 노란색 크기
                if yellow % j == 0 and yellow // j < w - 1:
                    return [w, h]


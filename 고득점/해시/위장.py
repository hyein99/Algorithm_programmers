from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for c in clothes:
        clothes_dict[c[1]] += 1

    result = 1
    for c_key in clothes_dict:
        result *= clothes_dict[c_key] + 1

    return result - 1
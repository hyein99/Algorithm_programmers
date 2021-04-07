from collections import defaultdict

# 풀이 1) 해시 사용
def solution(phone_book):
    phone_dict = defaultdict(int)
    for phone in phone_book:
        phone_dict[phone] = True

    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone_dict[phone[:i]]:
                return False

    return True

# 풀이 2) 시간초과
# def solution(phone_book):
#     for phone in phone_book:
#         for i in range(1, len(phone)):
#             if phone[:i] in phone_book:
#                 return False
#
#     return True
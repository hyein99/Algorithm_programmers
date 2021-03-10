# from collections import deque
#
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#
#     # 그래프화
#     words.append(begin)
#     for i in range(len(words)):
#         for j in range(words):
#             pass
#
#     def changeable(w1, w2):
#         cnt = 0
#         for i in range(len(w1)):
#             if w1[i] != w2[i]:
#                 cnt += 1
#         if cnt > 1:
#             return False
#         else:
#             return True
#
#     process = []
#
#     def dfs(word):
#         wlist = [w for w in words if changeable(word, w)]
#         while wlist:
#             tmp = wlist.pop(0)
#             if tmp == target:
#                 return len(process)
#             dfs(tmp)
#         process.append(word)
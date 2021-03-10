# from collections import defaultdict
# import heapq
#
# def solution(N, number):
#     dp = defaultdict(lambda: 9)
#     dp[0] = 0
#     cnt = 1
#     tmp = N
#     Q = [[0, 0]]
#     while cnt < 9:
#         if tmp == number:
#             return cnt
#         dp[tmp] = cnt
#         heapq.heappush(Q, [cnt, tmp])
#         tmp = tmp*10+N
#         cnt += 1
#
#     while Q: # cnt 낮은 순으로 뽑음
#         cnt, num = heapq.heappop(Q)
#         if cnt > 7:
#             break
#         oplist = [num+N, num-N, num*N, num//N]
#         for op in oplist:
#             if op == number:
#                 return cnt + 1
#             if dp[op] > cnt+1:
#                 dp[op] = cnt + 1
#                 heapq.heappush(Q, [cnt+1, op])
#
#     return -1
#
# # print(solution(5, 12))
# # print(solution(2, 11))
# # print(solution(5, 25))
# # print(solution(5, 23))
# print(solution(5, 87))
# # print(solution(5, 27))
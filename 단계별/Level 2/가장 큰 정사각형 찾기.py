# 풀이 1) 완전탐색 >> 시간초과
# def solution(board):
#     def possible(i, j, cnt):
#         for x in range(i, i + cnt):
#             for y in range(j, j + cnt):
#                 if x >= N or y >= M or not board[x][y]:
#                     return False
#         return True
#
#     N = len(board)
#     M = len(board[0])
#     answer = 0
#
#     for i in range(N):
#         for j in range(M):
#             if board[i][j]:
#                 cnt = 1
#                 while possible(i, j, cnt + 1):
#                     cnt += 1
#                 # print(i, j, cnt)
#                 answer = max(answer, cnt * cnt)
#
#     return answer

# 풀이 2) 완전탐색 >> 시간초과
# def solution(board):
#     def find_rec(x, y):
#         n = N   # 리턴할 정사각형의 길이
#         nx = x
#         while nx < N and nx < x + n and board[nx][y]:
#             ny = y
#             while ny < M and board[nx][ny]:
#                 ny += 1
#             if ny != y: # board[nx][ny]가 0이면 n이 0이되므로
#                 n = min(n, ny - y) # 가능한 정사각형 길이
#                 nx += 1
#         n = min(n, nx - x)         # x가 가능한 정사각형 길이
#
#         return n
#
#     N = len(board)
#     M = len(board[0])
#     answer = 0
#
#     for i in range(N):
#         for j in range(M):
#             if board[i][j]:
#                 cnt = find_rec(i, j)
#                 answer = max(answer, cnt * cnt)
#
#     return answer

# 풀이 3) 다이나믹프로그래밍
def solution(board):
    N = len(board)
    M = len(board[0])
    answer = 0

    for i in range(N):
        for j in range(M):
            if i==0 or j==0:
                if answer==0 and board[i][j]:
                    answer = 1
                continue
            if board[i][j]:
                cnt = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                board[i][j] = cnt
                answer = max(answer, cnt * cnt)

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
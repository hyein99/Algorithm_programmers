from collections import defaultdict

# 2진법으로 바꾸는 형식으로 구하기
def solution(n):
    cost = 0
    while n:
        if n%2:
            cost += 1
            n -= 1
        else:
            n //= 2
    return cost

# 하향식: 시간초과
# def solution(n):
#     def move(x):
#         if dp[x]:
#             return dp[x]
#
#         if x % 2:
#             dp[x] = move(x - 1) + 1
#         else:
#             dp[x] = move(x // 2)
#
#         return dp[x]
#
#     dp = defaultdict(int)
#     dp[1] = 1
#     return move(n)


# 상향식: 시간초과
# def solution(n):
#     dp = defaultdict(int)
#     if n==1:
#         return 1
#     dp[1] = 1
#
#     for i in range(2, n+1):
#         if i%2:
#             dp[i] = dp[i-1]+1
#         else:
#             dp[i] = dp[i//2]
#
#     return dp[n]
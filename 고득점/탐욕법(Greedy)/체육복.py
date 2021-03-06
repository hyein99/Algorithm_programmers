def solution(n, lost, reserve):
    L = set(lost)-set(reserve)
    R = set(reserve)-set(lost)

    for r in R:
        if r-1 in L:
            L.remove(r-1)
        elif r+1 in L:
            L.remove(r+1)

    return n - len(L)


# def solution(n, lost, reserve):
#     L = set(lost)-set(reserve)
#     R = set(reserve)-set(lost)
#
#     cnt, i, j = 0, 0, 0
#     while i < len(L) and j < len(R):
#         if R[j] - 1 > L[i]:
#             cnt += 1
#             i += 1
#         elif R[j] + 1 < L[i]:
#             j += 1
#         else:
#             i += 1
#             j += 1
#     cnt += len(L) - i
#
#     return n - cnt

# print(solution(n=5, lost=[2,4], reserve=[1,3,5]))
# print(solution(n=5, lost=[2,4], reserve=[3]))
print(solution(n=7, lost=[2,3,4], reserve=[1,2,3,6]))
print(solution(n=5, lost=[1,2,3], reserve=[2,3,4]))
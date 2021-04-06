def solution(s):
    st = []
    for i in range(len(s)):
        if st and st[-1] == s[i]:
            st.pop()
        else:
            st.append(s[i])
    if st:
        return 0
    else:
        return 1

# 시간초과
# def solution(s):
#     while s:
#         changed = False
#         i = 0
#         while i+1 < len(s):
#             if s[i] == s[i+1]:
#                 s = s.replace(s[i]+s[i+1], '')
#                 changed = True
#             else:
#                 i += 1
#         if not changed:
#             return 0
#     return 1
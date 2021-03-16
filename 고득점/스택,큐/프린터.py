from collections import deque

def solution(priorities, location):
    st = deque(priorities)
    cnt = 1
    while st:
        J = st.popleft()
        if not st:
            return cnt
        if J >= max(st):
            if location == 0:
                break
            location -= 1
            cnt += 1
        else:
            st.append(J)
            if location == 0:
                location = len(st)-1
            else:
                location -= 1
    return cnt
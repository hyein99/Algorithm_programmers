def solution(triangle):
    nxt = []
    for tri in triangle:
        nxt = [0]+nxt+[0]
        for i in range(len(tri)):
            tri[i] += max(nxt[i], nxt[i+1])
        nxt = tri
    return max(nxt)
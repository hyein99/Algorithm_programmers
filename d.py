from collections import defaultdict
# from collections import deque
import heapq
import sys


# 똑같은 함정 방을 두 번째 방문하게 되면 원래 방향의 길로 돌아옵니다.
def solution(n, start, end, roads, traps):
    def bfs(start, end):
        min_time = sys.maxsize
        Q = []
        heapq.heappush(Q, (0, start, 1))

        while Q:
            time, node, num = heapq.heappop(Q)

            # 최소시간을 초과하는 경우
            if time > min_time:
                continue

            # 도착한 경우
            if node == end:
                min_time = min(min_time, time)

            # trap 여부 확인
            next_num = num
            if node in trap_dict:

                if trap_dict[node] == 0:
                    trap_dict[node] = 1
                    if next_num == 2:
                        next_num = 1
                    else:
                        next_num = 2
                else:
                    trap_dict[node] = 0
                    next_num = 1

            # node에 연결된 다른 node 탐색
            if next_num == 1:
                for next_node, t in map1[node]:
                    if time + t < min_time:
                        heapq.heappush(Q, (time+t, next_node, next_num))
            else:
                for next_node, t in map2[node]:
                    if time + t < min_time:
                        heapq.heappush(Q, (time+t, next_node, next_num))

        return min_time

    # step 1) 두개 케이스의 map 생성
    map1 = defaultdict(list)
    map2 = defaultdict(list)
    for P, Q, S in roads:
        map1[P].append((Q, S))
        map2[Q].append((P, S))

    # step 2) trap 방문 여부를 알 수 있는 딕셔너리 생성
    trap_dict = dict()
    for t in traps:
        trap_dict[t] = 0

    # step 3) 최단 거리 계산
    answer = bfs(start, end)
    return answer

# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
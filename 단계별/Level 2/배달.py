from collections import defaultdict
from collections import deque

# 풀이 1) bfs: 시간초과(-6)
# 이전에 방문한 곳 고려하지 않음
# def solution(N, road, K):
#     def bfs():
#         qu = deque()
#         qu.append((1, 0)) # (node, 시간)
#         done = set()
#         done.add(1)
#
#         while qu:
#             node, t = qu.popleft()
#             for next_node, next_t in road_graph[node]:
#                 if t+next_t <= K and next_node != 1:
#                     done.add(next_node)
#                     qu.append((next_node, t+next_t))
#
#         return len(done)
#
#     # 입력
#     road_graph = defaultdict(list)
#     for fr, to, r in road:
#         road_graph[fr].append((to, r))
#         road_graph[to].append((fr, r))
#
#     return bfs()

# 풀이 2) dfs: 시간초과(-1)
# 이전에 방문 한 곳 고려함
# def solution(N, road, K):
#     def dfs(node, t):
#         for next_node, next_t in road_graph[node]:
#             if t + next_t <= K and not visited[next_node]:
#                 result.add(next_node)
#                 visited[next_node] = 1
#                 dfs(next_node, t + next_t)
#                 visited[next_node] = 0
#
#     # 입력
#     road_graph = defaultdict(list)
#     for fr, to, r in road:
#         road_graph[fr].append((to, r))
#         road_graph[to].append((fr, r))
#
#     result = set()
#     result.add(1)
#     visited = [0] * (N + 1)
#     visited[1] = 1
#
#     dfs(1, 0)
#
#     return len(result)

# 풀이 3) bfs: 통과
# 이전에 방문했어도 더 짧은 시간내 방문했으면 qu에 넣어줌줌
def solution(N, road, K):
    def bfs():
        qu = deque()
        qu.append((1, 0)) # (node, 시간)
        done = {1: 0}     # done[node] = 시간(<=K)

        while qu:
            node, t = qu.popleft()
            for next_node, next_t in road_graph[node]:
                # 처음 추가되는 경우 or 이전에 next_node에 도착한 시간보다 짧은 경우
                if (t+next_t <= K and next_node not in done) or (next_node in done and done[next_node] > t+next_t):
                    done[next_node] = t+next_t
                    qu.append((next_node, t+next_t))

        return len(done)


    # 입력
    road_graph = defaultdict(list)
    for fr, to, r in road:
        road_graph[fr].append((to, r))
        road_graph[to].append((fr, r))

    return bfs()
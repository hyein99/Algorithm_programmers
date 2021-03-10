from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    print(graph)

    route = []
    def dfs(city):
        while graph[city]:
            dfs(graph[city].pop(0))

        route.append(city)

    dfs('ICN')
    return route[::-1]

# print(solution(tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(solution(tickets = [["ICN","OUL"],["ICN","NRT"],["OUL","ICN"]]))
print(solution(tickets = [["ICN","OUL"],["ICN","NRT"],["NRT","ICN"]]))
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    cnt = 0
    i = 0
    while i < len(truck_weights):
        cnt += 1
        w = bridge.popleft()
        weight += w
        if truck_weights[i] <= weight:
            bridge.append(truck_weights[i])
            weight -= truck_weights[i]
            i += 1
        else:
            bridge.append(0)

    return cnt+bridge_length

print(solution(bridge_length=5, weight=5, truck_weights=[2, 2, 2, 2, 1, 1, 1, 1, 1]))
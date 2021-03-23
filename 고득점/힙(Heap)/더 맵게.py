import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        if food1 >= K and food2 >= K:
            break
        new_food = food1 + food2 * 2
        heapq.heappush(scoville, new_food)
        cnt += 1

        # 남은 음식이 1개 이하일 때
        if len(scoville) < 2 and new_food < K:
            return -1

    return cnt
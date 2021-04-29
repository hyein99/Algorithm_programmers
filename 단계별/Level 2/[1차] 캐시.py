from collections import deque


def solution(cacheSize, cities):
    # cache hit: 메모리에 존재할 경우
    # cache miss: 메모리에 존재하지 않을 경우
    if cacheSize == 0:
        return 5 * len(cities)

    cache = deque()
    result = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            result += 1
        else:
            if len(cache) < cacheSize:
                cache.append(c)
                result += 5
            else:
                cache.popleft()
                cache.append(c)
                result += 5

    return result
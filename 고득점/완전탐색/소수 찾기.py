def solution(numbers):
    def dfs(sub):
        if len(sub) == len(numbers):
            numset.add(int(sub))
            return

        for i in range(len(numbers)):
            numset.add(int(sub))
            if used[i] == 0:
                used[i] = 1
                dfs(sub + numbers[i])

                used[i] = 0

    def isPrime(n):
        if n < 2:
            return False
        x = int(n ** (1 / 2))
        for i in range(2, x + 1):
            if n % i == 0:
                return False
        return True

    # step 1: numbers로 만들 수 있는 자연수
    numset = set()
    used = [0] * len(numbers)
    for i in range(len(numbers)):
        used[i] = 1
        dfs(numbers[i])
        used[i] = 0

    # step 2: 소수 인지 판단
    cnt = 0
    for s in numset:
        # print(s)
        if isPrime(s):
            cnt += 1

    return cnt
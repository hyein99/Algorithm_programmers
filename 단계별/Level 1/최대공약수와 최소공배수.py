def solution(n, m):
    gcd = 1
    i = 2
    while i <= n:
        if n % i == 0 and m % i == 0:
            gcd *= i
            n //= i
            m //= i
        else:
            i += 1
    lcm = gcd * n * m

    return [gcd, lcm]
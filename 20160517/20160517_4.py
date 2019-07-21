def lattice(n, m):
    s = 1
    for i in range(n+m, m, -1):
        s *= i
    for i in range(n, 0, -1):
        s //= i
    return s

t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()[:2]]
    print(lattice(n, m) % (10**9+7))

def lattice(n, m):
    a = [1 for _ in range(n+1)]
    for _ in range(m):
       b = []
       for i in range(n+1):
           b.append(b[i-1] + a[i] if i > 0 else 1)
       a = b
    return a[-1]

t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()[:2]]
    print(lattice(n, m) % (10**9+7))

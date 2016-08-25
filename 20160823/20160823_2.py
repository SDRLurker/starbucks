def d(n):
    s = []
    for i in range(1, n//2+1):
        if n%i == 0:
            s.append(i)
    return sum(s)

res = set()
for t in range(int(input())):
    N = int(input())
    for a in range(1, N):
        b = d(a)
        if a != b and d(b) == a:
            res.add(a)
            if b < N:
                res.add(b)
    print(sum(res))

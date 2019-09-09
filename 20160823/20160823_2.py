def d(n):
    ds = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            ds.append(i)
            if n // i != i:
                ds.append(n//i)
    return sum(ds)

amicables = set()
for a in range(1,100000+1):
    b = d(a)
    if a != b and d(b) == a:
        if b > a:
            a, b = b, a
        amicables.add((a,b))

T = int(input())
for _ in range(T):
    N = int(input())
    s = 0
    for a,b in amicables:
        if a<=N:
            s += a
        if b<=N:
            s += b
    print(s)

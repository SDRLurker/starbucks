def d(n):
    s = [1]
    i = 2
    while i * i <= n: 
        if n % i != 0:
            i += 1 
            continue
        s.append(i)
        if i * i != n: 
            s.append(n//i)
        i += 1 
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
def spiral_sum(n):
    i = 3
    s = 1
    while i <= n:
        ii = i ** 2
        down = ii - (6 * ((i-1)//2) )        
        s += (ii + down) * 2
        i += 2
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    print(spiral_sum(n) % (10**9+7))

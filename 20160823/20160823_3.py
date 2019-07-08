# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap
    
def get_days(d_tuple):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y = d_tuple[0]
    m = d_tuple[1] - 1
    d = d_tuple[2] - 1
    cnt = 0
    iy = 1900
    while iy + 2800 < y:
        iy += 2800
    
    while iy < y:        
        cnt += 366 if is_leap(iy) else 365
        iy += 1
    
    im = 0
    days[1] = 29 if is_leap(iy) else 28    
    while im < m:
        cnt += days[im]
        im += 1
        
    return cnt
  
def get_num_sundays(start, end):
    s = list(start)
    cnt = 0
    while s <= list(end):        
        if get_days(s) % 7 == 6:
            #if s[1] == 4:
            #    print(s, cnt)
            cnt += 1
        if s[1] + 1 > 12:
            s[0] += 1
            s[1] = 1
        else:
            s[1] += 1
    return cnt
    
c = int(input())
for _ in range(c):
    s = input()
    e = input()
    start = s.split()
    end = e.split()
    y1 = int(start[0])
    m1 = int(start[1])
    d1 = int(start[2])
    y2 = int(end[0])
    m2 = int(end[1])
    d2 = int(end[2])
    print( get_num_sundays((y1,m1,d1), (y2,m2,d2)) )


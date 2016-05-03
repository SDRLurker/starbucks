#!/usr/bin/python
# -*- coding: utf-8 -*-

# 이진탐색으로 풀기
# 참고주소 : http://blog.eairship.kr/246
def binary_search(data_arr, item):
        low = 0
        high = len(data_arr)-1
        while low<=high:
                mid = (low+high) // 2
                if data_arr[mid][0] > item:
                        high = mid - 1
                elif data_arr[mid][0] < item:
                        low = mid + 1
                else:
                        return mid
        return -1

# 이진탐색으로 풀이한 결과 test 2의 경우
# 0.63초에서 0.09초로 빨라짐을 확인하였음.
def ice(m, n, c):
        data_arr = []
        i = 0
        while i < n:
                data_arr.append((c[i],i+1))
                i += 1
        data_arr = sorted(data_arr)
        i = 0
        while i < n:
                rest = data_arr[:i] + data_arr[i+1:]
                item = m - data_arr[i][0]
                idx = binary_search(rest, item)
                if idx >= 0:
                        return data_arr[i][1], rest[idx][1]
                i += 1

t = int(raw_input())
for _ in range(t):
        m = int(raw_input())
        n = int(raw_input())
        s = raw_input()
        c = [int(x) for x in s.split()]
        a,b = ice(m,n,c)
	# index값이 작은 값을 먼저 출력하기 위해 swap연산.
        if a > b:
                a,b = b,a
        print a,b


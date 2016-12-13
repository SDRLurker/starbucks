class Solution(object):
    def bsearch(self, array, v):
        l = 0
        r = len(array) - 1
        m = (l+r) // 2
        while l <= r:
            m = (l+r) // 2
            if array[m] > v:
                r = m - 1
            elif array[m] < v:
                l = m + 1
            else:
                return m,m
        return l,r
        
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        m = 0
        for h in houses:
            l,r = self.bsearch(heaters, h)
            if l != r:
                a = max(m, abs(heaters[l] - h)) if 0 <= l < len(heaters) else 0
                b = max(m, abs(heaters[r] - h)) if 0 <= r < len(heaters) else 0
                b = a if a > 0 and b == 0 else b
                a = b if b > 0 and a == 0 else a
                m = max(m, min(a,b))
        return m

def solve_string(s, houses, heaters, expected):
    return "%20s %20s %10d %10d" % (houses, heaters, expected, s.findRadius(houses, heaters))

s = Solution()
print("%20s %20s %10s %10s" % ("houses", "heaters", "Expected", "Result"))
print(solve_string(s, [1,2,3], [2], 1))
print(solve_string(s, [1,2,3,4], [1,4], 1))
print(solve_string(s, [1,2,3,4], [1,2], 2))

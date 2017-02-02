class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        m = 1
        sqrt_area = int(area ** 0.5)
        for d in range(1, sqrt_area+1):
            if area % d == 0:
                m = max(m, d)
        return [area // m, m]

def solve_string(s, area, expected):
    return "%10d %10s %10s" % (area, expected, s.constructRectangle(area))

s = Solution()
print("%10s %10s %10s" % ("area", "Expected", "Result"))
print(solve_string(s, 4, [2,2]))
print(solve_string(s, 1, [1,1]))
print(solve_string(s, 30, [6,5]))

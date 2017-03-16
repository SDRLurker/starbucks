class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        mins = []
        m = 9999
        for tp in timePoints:
            ms = tp.split(":")
            t = int(ms[0]) * 60 + int(ms[1])
            mins.append(t)
        mins.sort()
        for i in range(len(mins)):
            diff = abs(mins[(i+1)%len(mins)] - mins[i])
            if diff > 720:
                diff = abs(diff - 1440)
            m = min(diff, m)
        return m


def solve_string(s, timePoints, expected):
    return "%40s %10d %10d" % (timePoints, expected, s.findMinDifference(timePoints))

s = Solution()
print("%40s %10s %10s" % ("timePoints", "Expected", "Result"))
print(solve_string(s, ["23:59","00:00"], 1))
print(solve_string(s, ["05:31","22:08","00:35"], 147))

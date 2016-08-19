class Solution(object):
    def compare(self, a, b):
        return 0 if a-b == 0 else (a-b) // abs(a-b)
        
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        for i, lvl in enumerate(ver1):
            if i >= len(ver2):
                break
            a = self.compare(int(lvl), int(ver2[i]))
            if a != 0:
                return a
        a = self.compare(len(ver1), len(ver2))
        if a < 0:
            ver1, ver2 = ver2, ver1
        if a != 0:
            for i in range(len(ver2), len(ver1)):
                b = self.compare(int(ver1[i]), 0)
                if b != 0:
                    return b * a
            a = 0
        return a

def solve_string(s, ver1, ver2, expected):
	return "%10s %10s %10d %10d" % (ver1, ver2, expected, s.compareVersion(ver1, ver2))

s = Solution()
print("%10s %10s %10s %10s" % ("version1", "version2", "Expected", "Result"))
print(solve_string(s, "1.0", "1", 0))
print(solve_string(s, "1", "1.1", -1))
print(solve_string(s, "1.1", "1.01.0", 0))
print(solve_string(s, "1.0.1", "1", 1))
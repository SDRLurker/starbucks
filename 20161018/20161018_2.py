class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        numbers = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        c_cnt = [0 for x in range(26)]
        for c in s:
            c_cnt[ord(c)-ord('a')] += 1
        num_str = ""
        for si, n in enumerate(numbers):
            stay = True
            while stay:
                for c in n:
                    if c_cnt[ord(c)-ord('a')] == 0:
                        stay = False
                        break
                if stay:
                    for c in n:
                        c_cnt[ord(c)-ord('a')] -= 1
                    num_str += str(si)
        return num_str

def solve_string(solution, s, expected):
	return "%40s %10s %10s" % (s, expected, solution.originalDigits(s))

s = Solution()
print("%40s %10s %10s" % ("s", "Expected", "Result"))
print(solve_string(s, "owoztneoer", "012"))
print(solve_string(s, "fviefuro", "45"))
print(solve_string(s, "twonine", "29"))
print(solve_string(s, "zeroonetwothreefourfivesixseveneightnine", "0123456789"))
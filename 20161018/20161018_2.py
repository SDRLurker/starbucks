class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        evens = ("zero", "two", "four", "six", "eight")
        odds = ("one", "three", "five", "seven", "nine")
        c_cnt = [0 for x in range(26)]
        d_cnt = [0 for x in range(10)]
        for c in s:
            c_cnt[ord(c)-ord('a')] += 1
        for i, tup in enumerate((evens, odds)):
            for si, n in enumerate(tup):
                stay = True
                while stay:
                    for c in n:
                        if c_cnt[ord(c)-ord('a')] == 0:
                            stay = False
                            break
                    if stay:
                        for c in n:
                            c_cnt[ord(c)-ord('a')] -= 1
                        d_cnt[si*2+i] += 1
        num_str = ""
        for i, d in enumerate(d_cnt):
            num_str += (d * str(i))
        return num_str

def solve_string(solution, s, expected):
	return "%40s %10s %10s" % (s, expected, solution.originalDigits(s))

s = Solution()
print("%40s %10s %10s" % ("s", "Expected", "Result"))
print(solve_string(s, "owoztneoer", "012"))
print(solve_string(s, "fviefuro", "45"))
print(solve_string(s, "twonine", "29"))
print(solve_string(s, "zeroonetwothreefourfivesixseveneightnine", "0123456789"))
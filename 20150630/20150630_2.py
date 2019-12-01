class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)
        res = ""
        minus = False
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        if numerator < 0:
            minus = True
            numerator = -numerator 
            res = "-" if minus else ""
        res += str(numerator // denominator) + "."
        numerator = numerator % denominator
        quotients = []
        dividend = numerator * 10
        dividends = [dividend]
        start = 0
        repeat = True
        while dividend >= 10:
            if dividend % denominator == 0:
                res += "".join([str(i) for i in quotients]) + str(dividend//denominator)
                repeat = False
                break
            else:
                quotient = dividend // denominator
                dividend -= (denominator * quotient)
                dividend *= 10
                quotients.append(quotient)
                if dividend not in dividends:
                    dividends.append(dividend)
                else:
                    start = dividends.index(dividend)
                    break
        if repeat:
            if start > 0:
                res += "".join([str(i) for i in quotients[:start]])
            if len(quotients[start:]) > 0:
                res += "(" + "".join([str(i) for i in quotients[start:]]) + ")"
        return res

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.fractionToDecimal(1, 2), "0.5")
        self.assertEqual(s.fractionToDecimal(2, 1), "2")
        self.assertEqual(s.fractionToDecimal(2, 3), "0.(6)")
        self.assertEqual(s.fractionToDecimal(1, 6), "0.1(6)")
        self.assertEqual(s.fractionToDecimal(1, 4), "0.25")
        self.assertEqual(s.fractionToDecimal(1, 8), "0.125")
        self.assertEqual(s.fractionToDecimal(-50, 8), "-6.25")
        self.assertEqual(s.fractionToDecimal(7, -12), "-0.58(3)")

if __name__ == "__main__":
    unittest.main()

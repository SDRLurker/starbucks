class Solution:
    def selfDividingNumbers(self, left, right):
        nums = []
        for n in range(left, right+1):
            if 1<=n<10:
                nums.append(n)
            else:
                is_divide = True
                nn = n
                while n > 0:
                    if n%10 == 0 or nn % (n%10) != 0:
                        is_divide = False
                        break
                    n //= 10
                if is_divide:
                    nums.append(nn)
        return nums

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(1, 22), [1,2,3,4,5,6,7,8,9,11,12,15,22])

if __name__ == "__main__":
    unittest.main()

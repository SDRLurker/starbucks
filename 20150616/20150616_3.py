class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ss = [str(n)*3 for n in nums]
        ss.sort(reverse=True)
        ss = [s[:len(s)//3] for s in ss]
        s = "".join(ss).lstrip("0")
        return "0" if s == "" else s


import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.largestNumber([10,2]), "210")
        self.assertEqual(s.largestNumber([3,30,34,5,9]), "9534330")
        self.assertEqual(s.largestNumber([0,0]), "0")
        self.assertEqual(s.largestNumber([0]), "0")

if __name__ == "__main__":
    unittest.main()

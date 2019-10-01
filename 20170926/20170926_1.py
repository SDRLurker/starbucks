class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profits = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            max_profits += (peak - valley)
        return max_profits

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]),7)
        self.assertEqual(s.maxProfit([1,2,3,4,5]),4)
        self.assertEqual(s.maxProfit([7,6,4,3,1]),0)
        self.assertEqual(s.maxProfit([]),0)

if __name__ == "__main__":
    unittest.main()

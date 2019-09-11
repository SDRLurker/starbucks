# https://www.youtube.com/watch?v=DJ4a7cmjZY0&t=593s
class Solution(object):
    def __init__(self):
        self.ways = [0 for _ in range(100000+1)]
        self.ways[0] = 1
        for coin in (1,2,5,10,20,50,100,200):
            for i in range(1,len(self.ways)):
                if i - coin >= 0:
                    self.ways[i] += self.ways[i - coin]
    def coin_sum(self, s):
        return self.ways[s]

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.coin_sum(10), 11)
        self.assertEqual(s.coin_sum(15), 22)
        self.assertEqual(s.coin_sum(20), 41)

if __name__ == "__main__":
    s = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(s.coin_sum(N) % (10**9+7))

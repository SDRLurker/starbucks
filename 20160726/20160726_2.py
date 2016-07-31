class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = coins
        self.coins.sort(reverse=True)
        self.amount = amount
        self.min_num = -1
	self.min_k = amount+1
        self.backtrack([0 for x in xrange(amount)], 0)
        return self.min_num
        
    def backtrack(self, used_coins, k):
        if self.is_a_solution(used_coins, k):
            num = sum([1 for c in used_coins[0:k] if c > 0])
            if self.min_num == -1 or (num > 0 and self.min_num > num) :
                self.min_num = num
		self.min_k = k
        else:
            k = k + 1
            if k >= self.min_k:
                return
            candidates = self.get_candidates(used_coins, k)
            for c in candidates:
                used_coins[k-1] = c
                self.backtrack(used_coins, k)
                
    def is_a_solution(self, used_coins, k):
        if sum(used_coins[0:k]) == self.amount:
            return True
        return False
        
    def get_candidates(self, used_coins, k):
        c=[]
        for coin in self.coins:
            if self.amount - sum(used_coins[0:k-1]) - coin >= 0:
                c.append(coin)
        return c

def solve_string(s, coins, amount, expected):
	return "%20s %10d %10d %10d" % (coins, amount, expected, s.coinChange(coins, amount))

s = Solution()
print "%20s %10s %10s %10s" % ("coins", "amount", "Expected", "Result")
print solve_string(s, [1], 0, 0) 
print solve_string(s, [1,2,5], 11, 3) 
print solve_string(s, [2], 3, -1) 
print solve_string(s, [1,4,5], 8, 2) 
print solve_string(s, [2,5], 11, 4) 
#print solve_string(s, [1,2,5], 100, 20) 

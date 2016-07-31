class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        used_coins = [ amount+1 for _ in xrange(amount) ]
	coins.sort(reverse = True)
        for coin in coins:
            i = amount - 1
            while i >= 0:
                if used_coins[i] <= amount:  
                    cnt = used_coins[i]
                    self.check_used_coins(coin, amount, used_coins, i, cnt)
                i -= 1
	    self.check_used_coins(coin, amount, used_coins, i, 0)
            first = False
        used_coins = [0] + used_coins
        last = used_coins[-1]
	return last if last <= amount else -1

    def check_used_coins(self, coin, amount, used_coins, i, cnt):
        while i < amount:
            i += coin
            if i >= amount:
                break
            cnt += 1
            if cnt < used_coins[i]:
                used_coins[i] = cnt
                    
def solve_string(s, coins, amount, expected):
	return "%20s %10d %10d %10d" % (coins, amount, expected, s.coinChange(coins, amount))

s = Solution()
print "%20s %10s %10s %10s" % ("coins", "amount", "Expected", "Result")
print solve_string(s, [1], 0, 0) 
print solve_string(s, [1], 1, 1) 
print solve_string(s, [1,2,5], 11, 3) 
print solve_string(s, [2], 3, -1) 
print solve_string(s, [1,4,5], 8, 2) 
print solve_string(s, [2,5], 11, 4) 
print solve_string(s, [1,2,5], 100, 20) 
print solve_string(s, [3,7,405,436], 8839, 25)

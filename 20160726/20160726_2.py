class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        used_coins = [ amount+1 for _ in xrange(amount) ]
        used_coins = [0] + used_coins
        coins.sort(reverse = True)
        for i in xrange(amount+1): 
            for coin in coins:
                if i < coin:
                    continue
                used_coins[i] = min(used_coins[i], used_coins[i-coin] + 1)
        last = used_coins[-1]
	return last if last <= amount else -1

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
print solve_string(s, [370,417,408,156,143,434,168,83,177,280,117], 9953, 24)
print solve_string(s, [84,457,478,309,350,349,422,469,100,432,188], 6993, 15)

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        num_ranks = []
        for i, num in enumerate(nums):
            num_ranks.append((num, i))
        num_ranks.sort(reverse=True)
        
        ranks = [None] * len(nums)
        for rank, num_rank in enumerate(num_ranks):
            if rank == 0:
                ranks[num_rank[1]] = "Gold Medal"
            elif rank == 1:
                ranks[num_rank[1]] = "Silver Medal"
            elif rank == 2:
                ranks[num_rank[1]] = "Bronze Medal"
            else:
                ranks[num_rank[1]] = str(rank + 1)
        return ranks

def solve_string(s, nums, expected):
    return "%15s %30s %30s" % (nums, expected, s.findRelativeRanks(nums))

s = Solution()
print("%30s %10s %10s" % ("nums", "Expected", "Result"))
print(solve_string(s, [5,4,3,2,1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]))
print(solve_string(s, [3,4,5,2,1], ["Bronze Medal","Silver Medal","Gold Medal","4","5"]))

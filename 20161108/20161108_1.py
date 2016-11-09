class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        nums.sort(reverse=True)
        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]
            c += (diff * (i+1))
        return c

def solve_string(s, nums, expected):
    import copy
    return "%40s %10d %10d" % (nums, expected, s.minMoves(copy.deepcopy(nums)))

s = Solution()
print("%40s %10s %10s" % ("nums", "Expected", "Result"))
print(solve_string(s, [1,2,3], 3))
print(solve_string(s, [1,2147483647], 2147483646))



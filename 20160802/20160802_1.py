class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums[1:]:
            nums[0] ^= num
        return nums[0]

def solve_string(s, nums, expected):
	return "%20s %10d %10d" % (nums, expected, s.singleNumber(nums))

s = Solution()
print "%20s %10s %10s" % ("input", "Expected", "Result")
print solve_string(s, [1], 1) 
print solve_string(s, [1,-1,1], -1) 
print solve_string(s, [1,2,3,2,1], 3) 


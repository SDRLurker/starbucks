class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        max_idx = nums[s]
        while s < len(nums) and nums[s] > 0:
            for i in xrange(s, max_idx+1):
                if nums[i] + i > max_idx:
                    max_idx = nums[i] + i
                if max_idx >= len(nums) - 1:
                    return True
            s += 1
            while s+1 < len(nums)-1 and nums[s] == 0:
                s += 1
        if max_idx >= len(nums) - 1:
            return True
        return False

def solve_string(s, nums, expected):
	return "%20s %10s %10s" % (nums, expected, s.canJump(nums))

s = Solution()
print "%20s %10s %10s" % ("input", "Expected", "Result")
print solve_string(s, [0], True)
print solve_string(s, [2,3,1,1,4], True)
print solve_string(s, [3,2,1,0,4], False)
print solve_string(s, [1,1,1,0], True)
print solve_string(s, [1,1,2,2,0,1,1], True)
print solve_string(s, [1,1,0,1], False)
print solve_string(s, [5,9,3,2,1,0,2,3,3,1,0,0], True)
print solve_string(s, [2,0,1,0,1], False)
print solve_string(s, [4,0,4,2,2,0,1,3,3,0,3], True)
print solve_string(s, [1,0,1,1], False)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
            else:
                nums[i-z] = nums[i]
        for i in range(z):
            nums[-1-i] = 0

def solve_string(s, nums, expected):
    import copy
    nums_copy = copy.deepcopy(nums)
    s.moveZeroes(nums_copy)
    return "%20s %20s %20s" % (nums, expected, nums_copy)

s = Solution()
print("%20s %20s %20s" % ("num", "Expected", "Result"))
print(solve_string(s, [0,1,0,3,12], [1,3,12,0,0]))
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            t = nums[i] - 1
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[t]:
                t = nums[i] - 1
                nums[i], nums[t] = nums[t], nums[i]
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                break
            i += 1
        return i+1

def solve_string(s, nums, expected):
        return "%30s %8d %8d" % (nums, expected, s.firstMissingPositive(nums))

s = Solution()
print("%30s %8s %8s" % ("nums", "Expected", "Result"))
print(solve_string(s, [], 1))
print(solve_string(s, [1,2,0], 3))
print(solve_string(s, [3,4,-1,1], 2))

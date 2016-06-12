class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = 0
        if len(nums) < 3:
            return False
        arr = [nums[0], 0]
        
        for num in nums:
            if num <= arr[idx]:
                if not (idx > 0 and num <= arr[idx-1]):
                    arr[idx] = num
            else:
                idx += 1
                if idx >= 2:
                    return True
                arr[idx]= num
        return False

s = Solution()
print "%20s %8s %8s" % ("nums", "Expected", "Result")
nums = [2,1,5,0,3]
print "%20s %8s %8s" % (str(nums), "False", s.increasingTriplet(nums))
nums = [1,2,-10,-8,-7]
print "%20s %8s %8s" % (str(nums), "True", s.increasingTriplet(nums))

import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
	first = second = sys.maxint
        
        for num in nums:
		if num <= first:
			first = num	
		elif num <= second:
			second = num
		else:
			return True
        return False

s = Solution()
print "%20s %8s %8s" % ("nums", "Expected", "Result")
nums = [2,1,5,0,3]
print "%20s %8s %8s" % (str(nums), "False", s.increasingTriplet(nums))
nums = [1,2,-10,-8,-7]
print "%20s %8s %8s" % (str(nums), "True", s.increasingTriplet(nums))

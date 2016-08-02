class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kv = {}
        for i, num in enumerate(nums):
	    kv[num] = i
        for num in nums:
            if target-num in kv:
                return [kv[num], kv[target-num]]
        return []

def solve_string(s, nums, target, expected):
	return "%20s %10d %10s %10s" % (nums, target, expected, s.twoSum(nums, target))

s = Solution()
print "%20s %10s %10s %10s" % ("nums", "target", "Expected", "Result")
print solve_string(s, [3,2,4], 6, [1,2]) 
print solve_string(s, [1,4,4,2], 8, [1,2]) 
print solve_string(s, [2,1,9,4,4,56,90,3], 8, [3,4])
print solve_string(s, [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789], 542, [28,45])

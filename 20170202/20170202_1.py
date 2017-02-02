class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_ones = 0
        ones_cnt = 0
        
        for num in nums:
            if num == 1:
                ones_cnt += 1
            elif num == 0:
                m_ones = max(m_ones, ones_cnt)
                ones_cnt = 0
        m_ones = max(m_ones, ones_cnt)
        return m_ones

def solve_string(s, nums, expected):
    return "%30s %10d %10d" % (nums, expected, s.findMaxConsecutiveOnes(nums))

s = Solution()
print("%30s %10s %10s" % ("nums", "Expected", "Result"))
print(solve_string(s, [1,1,0,1,1,1], 3))
print(solve_string(s, [1,0,1,1,0,1], 2))
print(solve_string(s, [1,0,1,1,1,1], 4))

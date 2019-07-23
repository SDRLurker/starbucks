class Solution:
    def findPairs(self, nums, k):
        pair_num = 0
        cnt_dic = {}
        for n in nums:
            cnt_dic[n] = cnt_dic.get(n, 0) + 1
        if k == 0:            
            for n in cnt_dic:
                if cnt_dic[n] > 1:
                    pair_num += 1
        elif k > 0:            
            key_list = list(cnt_dic.keys())
            key_list.sort()
            for n in key_list:
                if n+k in cnt_dic:
                    pair_num += 1                     
        return pair_num

def solve_string(s, nums, k, expected):
	return "%20s %10d %10d %10d" % (nums, k, expected, s.findPairs(nums, k))

s = Solution()
print("%20s %10s %10s %10s" % ("nums", "k", "expected", "Result"))
print(solve_string(s, [3,1,4,1,5], 2, 1))
print(solve_string(s, [1,2,3,4,5], 1, 4))
print(solve_string(s, [1,3,1,5,4], 0, 1))
print(solve_string(s, [1,2,3,4,5], -1, 0))
print(solve_string(s, [1,1,1,1,1], 0, 1))

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        output = []
        m = len(list1) + len(list2)
        list1_dic = {}
        for i, item in enumerate(list1):
            list1_dic[item] = i
        for i, item in enumerate(list2):
            if item in list1_dic and i + list1_dic[item] <= m:
                if len(output) > 0 and i + list1_dic[item] < m:
                    output.pop()
                output.append(item)
                m = i + list1_dic[item]
        return output

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        l2 = ["KFC","Shogun","Burger King"] 
        self.assertEqual(s.findRestaurant(l1, l2), ["Shogun"])
        l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        l2 = ["KFC","Burger King","Tapioca Express","Shogun"]
        o = ["KFC","Burger King","Tapioca Express","Shogun"]
        self.assertEqual(s.findRestaurant(l1, l2), o)

if __name__ == "__main__":
    unittest.main()

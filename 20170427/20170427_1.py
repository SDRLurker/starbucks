class Solution(object):
    def num_to_words(self, ns):
        """
        :type ns: str
        :rtype: str
        """
        n = int(ns)
        if n == 0:
            return "Zero"
        res = []
        d = (10**12, 10**9, 10**6, 10**3, 10**0)
        ds = ("Trillion", "Billion", "Million", "Thousand", "")
        for i, dv in enumerate(d):
            if n // dv > 0:
                tw = ("Zero", "One", "Two", "Three", "Four")
                tw += ("Five", "Six", "Seven", "Eight", "Nine")
                tw += ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen")
                tw += ("Fifteen","Sixteen","Seventeen","Eighteen","Nineteen")
                t = ("","","Twenty", "Thirty", "Forty", "Fifty", "Sixty") 
                t += ("Seventy", "Eighty", "Ninety") 
                h = (n // dv) % 1000
                if h // 100 > 0:
                    res.append(tw[h//100])
                    res.append("Hundred")
                if h % 100 >= 20:
                    res.append(t[h//10%10])
                    if h % 10 > 0:
                        res.append(tw[h%10])
                elif h > 0: 
                    res.append(tw[h%20])
                if h > 0:
                    res.append(ds[i])

        return " ".join(res).strip()

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        self.assertEqual(s.num_to_words("0"), "Zero")
        self.assertEqual(s.num_to_words("10"), "Ten")
        self.assertEqual(s.num_to_words("20"), "Twenty")
        self.assertEqual(s.num_to_words("31"), "Thirty One")
        self.assertEqual(s.num_to_words("123117"), "One Hundred Twenty Three Thousand One Hundred Seventeen")
        self.assertEqual(s.num_to_words("123456789"), "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine")
        self.assertEqual(s.num_to_words("10000000010"), "Ten Billion Ten")
        self.assertEqual(s.num_to_words("10000000010"), "Ten Billion Ten")
        self.assertEqual(s.num_to_words("104382426112"), "One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty Six Thousand One Hundred Twelve")
        self.assertEqual(s.num_to_words("1104382426112"), "One Trillion One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty Six Thousand One Hundred Twelve")

if __name__ == "__main__":
    unittest.main()

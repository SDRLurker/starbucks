class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        dtoa_dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }        
        indices = [0 for _ in range(len(digits))]
        res = []
        while True:
            sa = []
            for i, d in enumerate(digits):
                sa.append(dtoa_dic[d][indices[i]])
            res.append("".join(sa))
            ri = len(digits)-1
            is_break = False
            while indices[ri] == len(dtoa_dic[digits[ri]]) - 1:
                if ri == 0:
                    is_break = True
                    break
                indices[ri] = 0
                ri -= 1
            if is_break:
                break
            if indices[ri] < len(dtoa_dic[digits[ri]]) - 1:
                indices[ri] += 1            
        return res

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        exp = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(s.letterCombinations("23"), exp)
        self.assertEqual(s.letterCombinations(""), [])
        self.assertEqual(s.letterCombinations("7"), ['p','q','r','s'])
        exp =['jmpt',
        'jmpu',
        'jmpv',
        'jmqt',
        'jmqu',
        'jmqv',
        'jmrt',
        'jmru',
        'jmrv',
        'jmst',
        'jmsu',
        'jmsv',
        'jnpt',
        'jnpu',
        'jnpv',
        'jnqt',
        'jnqu',
        'jnqv',
        'jnrt',
        'jnru',
        'jnrv',
        'jnst',
        'jnsu',
        'jnsv',
        'jopt',
        'jopu',
        'jopv',
        'joqt',
        'joqu',
        'joqv',
        'jort',
        'joru',
        'jorv',
        'jost',
        'josu',
        'josv',
        'kmpt',
        'kmpu',
        'kmpv',
        'kmqt',
        'kmqu',
        'kmqv',
        'kmrt',
        'kmru',
        'kmrv',
        'kmst',
        'kmsu',
        'kmsv',
        'knpt',
        'knpu',
        'knpv',
        'knqt',
        'knqu',
        'knqv',
        'knrt',
        'knru',
        'knrv',
        'knst',
        'knsu',
        'knsv',
        'kopt',
        'kopu',
        'kopv',
        'koqt',
        'koqu',
        'koqv',
        'kort',
        'koru',
        'korv',
        'kost',
        'kosu',
        'kosv',
        'lmpt',
        'lmpu',
        'lmpv',
        'lmqt',
        'lmqu',
        'lmqv',
        'lmrt',
        'lmru',
        'lmrv',
        'lmst',
        'lmsu',
        'lmsv',
        'lnpt',
        'lnpu',
        'lnpv',
        'lnqt',
        'lnqu',
        'lnqv',
        'lnrt',
        'lnru',
        'lnrv',
        'lnst',
        'lnsu',
        'lnsv',
        'lopt',
        'lopu',
        'lopv',
        'loqt',
        'loqu',
        'loqv',
        'lort',
        'loru',
        'lorv',
        'lost',
        'losu',
        'losv']
        self.assertEqual(s.letterCombinations("5678"), exp)

if __name__ == "__main__":
    unittest.main()

# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_recur(n):
    d = 10
    p = []
    rr = []
    while True:
        r = d % n
        if r == 0:
            p = []
            break
        m = d // n
        #print(rr, d, r, m)
        if r in rr:
            if m in p:
                p = p[p.index(m):]
                break
        rr.append(r)
        p.append(m)
        d = r * 10
    return "".join([str(i) for i in p])

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(get_recur(2), "")
        self.assertEqual(get_recur(3), "3")
        self.assertEqual(get_recur(4), "")
        self.assertEqual(get_recur(5), "")
        self.assertEqual(get_recur(6), "6")
        self.assertEqual(get_recur(7), "142857")
        self.assertEqual(get_recur(8), "")
        self.assertEqual(get_recur(9), "1")
        self.assertEqual(get_recur(10), "")
        self.assertEqual(get_recur(11), "09")
        self.assertEqual(get_recur(12), "3")
        self.assertEqual(get_recur(13), "076923")
        self.assertEqual(get_recur(22), "45")
        self.assertEqual(get_recur(31), "032258064516129")
        self.assertEqual(get_recur(81), "012345679")
        self.assertEqual(get_recur(97), "010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567")
        self.assertEqual(get_recur(101), "0099")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        m = 0
        mi = -1
        for i in range(2,N+1):
            if is_prime(i) and len(get_recur(i)) > m:
                mi = i
                m = len(get_recur(i))
        print(mi)

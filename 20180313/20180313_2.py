# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_factors(n):
    factors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors
  
def is_pandigital(pro, n):
    factors = get_factors(pro)
    for a,b in factors:
        s = [str(a), str(b), str(pro)]
        ss = "".join(s)
        sss = "".join(sorted("".join(ss)))
        pp = "".join([str(j) for j in range(1,n+1)])
        if pp == sss:
            return True
    return False

def get_p_sum(n):
    s = 0
    for i in range(10,9999,2):
        if is_pandigital(i, n):
            s += i
    return s

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        self.assertEqual(get_p_sum(4), 12)
        self.assertEqual(get_p_sum(5), 52)
        self.assertEqual(get_p_sum(6), 162)
        self.assertEqual(get_p_sum(7), 0)
        self.assertEqual(get_p_sum(8), 13458)
        self.assertEqual(get_p_sum(9), 45228)

if __name__ == "__main__":
    unittest.main()

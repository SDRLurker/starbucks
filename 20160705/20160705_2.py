class Solution(object):
    converts = [0x0, 0x8, 0x4, 0xC, 0x2, 0xA, 0x6, 0xE, 0x1, 0x9, 0x5, 0xD, 0x3, 0xB, 0x7, 0xF]
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in xrange(8):
            result <<= 4
            result += self.converts[n&0xF]
            n >>= 4
        return result

s = Solution()
print "%20s %20s %20s" % ("Input", "Output", "Expected")
o = s.reverseBits(13)
e = 0xB0000000
print "%10d(%08X) %10d(%08X) %10d(%08X)" % (13, 13, o, o, e, e)
o = s.reverseBits(0)
e = 0
print "%10d(%08X) %10d(%08X) %10d(%08X)" % (0, 0, o, o, e, e)
o = s.reverseBits(1)
e = 0x80000000
print "%10d(%08X) %10d(%08X) %10d(%08X)" % (1, 1, o, o, e, e)

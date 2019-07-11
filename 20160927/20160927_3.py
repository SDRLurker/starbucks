class Solution(object):
    def _proc_str(self, res, ci, stack_is, s, i):
        if len(stack_is) % 2 == 1:
            stack_is.append(s[ci:i])
        elif len(stack_is) > 0:
            stack_is[-1] += s[ci:i]
        else:
            res += s[ci:i]
        ci = -1
        return res, ci
    def decodeString(self, s: str) -> str:
        stack_is = []
        di = -1
        ci = -1
        li = -1
        res = ""
        for i, c in enumerate(s):
            if c.isdigit():
                if di < 0:
                    di = i
                res, ci = self._proc_str(res, ci, stack_is, s, i)
            if c == '[':
                if len(stack_is) % 2 == 1:
                    stack_is.append('')
                stack_is.append(int(s[di:i]))
                di = -1
            if c.isalpha():
                if ci < 0:
                    ci = i
            if c == ']':
                res, ci = self._proc_str(res, ci, stack_is, s, i)
                chars = stack_is.pop()
                multi = stack_is.pop()
                if len(stack_is) == 0:
                    res += (chars*multi)
                else:
                    stack_is[-1] += (chars*multi)
                li = i
            #print(i,c,stack_is,res)
        if len(s) > 0 and s[-1].isalpha() and li >= 0:
            res += s[li+1:]
        if len(stack_is) == 0 and li < 0:
            res += s
        return res


def solve_string(s, i, expected):
    return "%15s %20s %20s" % (i, expected, s.decodeString(i))

s = Solution()
print("%15s %20s %20s" % ("n", "Expected", "Result"))
print(solve_string(s, "3[a]2[bc]", "aaabcbc"))
print(solve_string(s, "3[a2[c]]", "accaccacc"))
print(solve_string(s, "2[abc]3[cd]ef", "abcabccdcdcdef"))
print(solve_string(s, "3[a]2[b4[F]c]", "aaabFFFFcbFFFFc"))
print(solve_string(s, "sd2[f2[e]g]i", "sdfeegfeegi"))
print(solve_string(s, "leetcode", "leetcode"))
#print(solve_string(s, "3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"))

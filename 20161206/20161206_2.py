class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_cnt = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                s_cnt += 1
        
        b_cnt = 0
        s_dic = {}
        g_dic = {}
        for i in range(len(secret)):
            s_dic[secret[i]] = s_dic.get(secret[i], 0) + 1
            g_dic[guess[i]] = g_dic.get(guess[i], 0) + 1
        for k in s_dic:
            if k in g_dic:
                b_cnt += s_dic[k] if g_dic[k] >= s_dic[k] else g_dic[k]
        b_cnt -= s_cnt
        return "%dA%dB" % (s_cnt, b_cnt)

def solve_string(s, secret, guess, expected):
    return "%10s %10s %10s %10s" % (secret, guess, expected, s.getHint(secret, guess))

s = Solution()
print("%10s %10s %10s %10s" % ("secret", "guess", "Expected", "Result"))
print(solve_string(s, "1807", "7810", "1A3B"))
print(solve_string(s, "1123", "0111", "1A1B"))

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        def count(num):
            return (1+num) * num / 2
        res, cnt = 0, 0
        for c in s+'0':
            if c == '0':
                if cnt == 0:
                    continue
                else:
                    res += count(cnt)
                    res %= MOD
                    cnt = 0
            else:
                cnt += 1
        return res

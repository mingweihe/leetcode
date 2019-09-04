class Solution(object):
    def countBinarySubstrings(self, s):
        """
        011000111100000
        1+2+3+4
        """
        # s = map(len, s.replace('10', '1 0').replace('01', '0 1').split())
        # return sum(min(a, b) for a, b in zip(s, s[1:]))
        """
        no need to accumulate res everytime, accumulate when necessary
        """
        last = s[0]
        res = lastLen = curLen = 0
        for c in s:
            if c == last:
                curLen += 1
            else:
                last = c
                res += min(lastLen, curLen)
                lastLen = curLen
                curLen = 1
        res += min(lastLen, curLen)
        return res




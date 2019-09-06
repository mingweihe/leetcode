class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Approach 2
        res, dp, ds = [], [0] * 26, [0] * 26
        ls, lp = len(s), len(p)
        for i in range(lp): dp[ord(p[i]) - 97] += 1
        for i in range(ls):
            if i > lp - 1: ds[ord(s[i - lp]) - 97] -= 1
            ds[ord(s[i]) - 97] += 1
            if dp == ds: res.append(i - lp + 1)
        return res

        # Approach 1
        # return [i for i in range(len(s) - len(p) + 1) if sorted(s[i:i + len(p)]) == sorted(p)]

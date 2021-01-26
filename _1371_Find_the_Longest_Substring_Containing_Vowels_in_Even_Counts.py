class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {0: -1}
        state = 0
        aeiou = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res = 0
        for i, c in enumerate(s):
            if c in aeiou:
                state ^= 1<<aeiou[c]
            if state not in d:
                d[state] = i
            res = max(res, i-d[state])
        return res

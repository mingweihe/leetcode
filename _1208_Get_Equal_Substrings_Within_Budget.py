class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # Approach 2 sliding windows
        i = 0
        for j in xrange(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            if maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1

        # Approach 1 two pointers
        # L = len(s)
        # res, i, j = 0, 0, 0
        # summ = 0
        # while j < L:
        #     cur = abs(ord(s[j])-ord(t[j]))
        #     if summ + cur <= maxCost:
        #         summ += cur
        #         j += 1
        #         res = max(res, j-i)
        #     else:
        #         summ -= abs(ord(s[i])-ord(t[i]))
        #         i += 1
        # return res

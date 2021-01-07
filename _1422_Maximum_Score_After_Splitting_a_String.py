class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 2, one pass
        res , zeros, ones = -float('inf'), 0, 0
        for i, c in enumerate(s):
            if c == '0': zeros += 1
            else: ones += 1
            if i != len(s) - 1:
                res = max(res, zeros - ones)
        return res + ones
        
        ## Approach 1, two passes
        # cnt = Counter(s)
        # res, zeros = 0, 0
        # for i in xrange(len(s)-1):
        #     if s[i] == '0': zeros += 1
        #     past_ones = i - zeros + 1
        #     remaining_ones = cnt['1'] - past_ones
        #     res = max(res, zeros + remaining_ones)
        # return res

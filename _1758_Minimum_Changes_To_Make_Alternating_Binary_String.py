class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Approach 2
        r = sum(i & 1 ^ int(x) for i, x in enumerate(s))
        return min(r, len(s) - r)
    
        ## Approach 1
        # ans1 = 0
        # for i in xrange(len(s)):
        #     if i & 1:
        #         if s[i] == '1': ans1 += 1
        #     else:
        #         if s[i] == '0': ans1 += 1
        # ans2 = 0
        # for i in xrange(len(s)):
        #     if i & 1:
        #         if s[i] == '0': ans2 += 1
        #     else:
        #         if s[i] == '1': ans2 += 1
        # return min(ans1, ans2)

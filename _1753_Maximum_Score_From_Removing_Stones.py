class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ## Approach 2, O(1)
        a, b, c = sorted([a, b, c])
        if a + b < c: return a + b
        return a + b + c >> 1
    
        ## Approach 1, O(n)
        # res = 0
        # a, b, c = sorted([a, b, c])
        # while (a > 0) + (b > 0) + (c > 0) > 1:
        #     b -= 1
        #     c -= 1
        #     a, b, c = sorted([a, b, c])
        #     res += 1
        # return res

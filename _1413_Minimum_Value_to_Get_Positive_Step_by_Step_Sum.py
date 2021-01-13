class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Approach 2
        res, accum = 0, 0
        for x in nums:
            accum += x
            res = min(res, accum)
        return 1 - res
        
        ## Approach 1
        # res, accum = 1, 0
        # for x in nums:
        #     accum += x
        #     res = max(res, -accum + 1)
        # return res

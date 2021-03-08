from math import ceil


class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        ## Approach 2
        return (abs(sum(nums)-goal) + limit - 1) / limit
    
        ## Approach 1
        # offset = float(abs(sum(nums) - goal))
        # return int(ceil(offset/limit))

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach 1
        res, odds = 0, []
        for i, x in enumerate(nums):
            if x & 1: odds.append(i)
        for i in xrange(k-1, len(odds)):
            index_left = odds[i-k+1]
            index_right = odds[i]
            if i-k > -1:
                num_even_left = 0 if index_left == 0 else index_left - odds[i-k] - 1
            else:
                num_even_left = 0 if index_left == 0 else index_left
            if i+1 < len(odds):
                num_even_right = 0 if index_right == len(nums)-1 else odds[i+1] - index_right - 1
            else:
                num_even_right = 0 if index_right == len(nums)-1 else len(nums) - odds[i] - 1
            res += (num_even_left+1) * (num_even_right+1)
        return res

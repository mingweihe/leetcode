import fractions


class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach 2
        return reduce(fractions.gcd, nums) == 1
        # Approach 1
        # gcd = nums[0]
        # for x in nums:
        #     while x:
        #         gcd, x = x, gcd % x
        # return gcd == 1

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 2 (conciser)
        res = [1] * len(nums)
        for i in xrange(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        right_product = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] = res[i] * right_product
            right_product *= nums[i]
        return res

        # Approach 1
        # output = [1]*len(nums)
        # product = 1
        # for i in xrange(len(nums)-2, -1, -1):
        #     output[i] = output[i+1]*nums[i+1]
        # print output
        # for i in xrange(1, len(nums)):
        #     product *= nums[i-1]
        #     output[i] *= product
        # return output

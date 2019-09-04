class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2
        left_sum, right_sum = 0, sum(nums)
        for i, x in enumerate(nums):
            right_sum -= x
            if left_sum == right_sum:
                return i
            left_sum += x
        return -1
        # Approach 1
        # accum, total = 0, sum(nums)
        # for i, x in enumerate(nums):
        #     if accum * 2 == total - x:
        #         return i
        #     accum += x
        # return -1

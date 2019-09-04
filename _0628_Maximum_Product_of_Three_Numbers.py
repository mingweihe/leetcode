import heapq


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 3
        # nums.sort()
        # return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        # Approach 2
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
        # Approach 1
        # min1, min2 = float('inf'), float('inf')
        # max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        # for x in nums:
        #     if x < min2:
        #         min2 = x
        #         if min2 < min1:
        #             min1, min2 = min2, min1
        #     if x > max1:
        #         max1 = x
        #         if max1 > max2:
        #             max1, max2 = max2, max1
        #         if max2 > max3:
        #             max2, max3 = max3, max2
        # return max(min1 * min2 * max3, max1 * max2 * max3)


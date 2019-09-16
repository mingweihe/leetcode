class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        L = len(nums)
        res = 0
        for i in xrange(L - 2):
            left, right = i + 1, L - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res

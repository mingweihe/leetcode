class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i, j = 0, n
        res = []
        while i < n:
            res += nums[i],
            res += nums[j],
            i += 1
            j += 1
        return res

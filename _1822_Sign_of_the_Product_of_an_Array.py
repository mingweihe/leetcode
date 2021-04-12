class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = reduce(lambda x, y: x * y, nums)
        if x > 0: return 1
        if x < 0: return -1
        return 0

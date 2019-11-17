class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [0, -10 ** 9 - 2, -10 ** 9 - 1]
        for x in nums:
            for i in [x + n for n in seen]:
                seen[i % 3] = max(seen[i % 3], i)
        return seen[0]

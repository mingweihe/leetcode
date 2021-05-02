class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans = float('inf')
        for i, x in enumerate(nums):
            if x != target: continue
            if abs(i - start) < ans:
                ans = abs(i - start)
        return ans

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] > height[r]: r -= 1
            else: l += 1
        return res

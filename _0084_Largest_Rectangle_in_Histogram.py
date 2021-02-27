class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res, stack = 0, [-1]
        heights += 0,
        for i, x in enumerate(heights):
            while x < heights[stack[-1]]:
                idx = stack.pop()
                res = max(res, heights[idx] * (i - stack[-1] - 1))
            stack += i,
        return res

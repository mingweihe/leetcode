class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res, L = 0, len(heights)
        stack = []
        for i in xrange(L+1):
            h = 0 if i == L else heights[i]
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                start = -1 if not stack else stack[-1]
                res = max(res, height*(i-start-1))
            stack.append(i)
        return res

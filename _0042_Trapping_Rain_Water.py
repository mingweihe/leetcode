class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ## Approach 2
        res, l, r, max_left, max_right = 0, 0, len(height)-1, 0, 0
        while l <= r:
            if max_left <= max_right:
                max_left = max(max_left, height[l])
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1
        return res

        ## Approach 1
        # res, stack = 0, []
        # for i, x in enumerate(height):
        #     while stack and x > height[stack[-1]]:
        #         idx = stack.pop()
        #         if not stack: continue
        #         res += (min(x, height[stack[-1]]) - height[idx]) * (i - stack[-1] - 1)
        #     stack += i,
        # return res

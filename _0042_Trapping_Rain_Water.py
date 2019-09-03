class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Approach 1
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res
        # Approach 2
        # res = 0
        # i = 0
        # stack = []
        # while i < len(height):
        #     if not stack or height[i] <= height[stack[-1]]:
        #         stack.append(i)
        #         i += 1
        #     else:
        #         bot = stack.pop()
        #         if not stack: continue
        #         H = min(height[i], height[stack[-1]]) - height[bot]
        #         cur_water = H * (i-stack[-1]-1)
        #         res += cur_water
        # return res

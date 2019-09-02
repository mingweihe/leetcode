class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1 greedy 投石问路!!!
        res, predicted_max, maximum = 0, 0, 0
        for i in xrange(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if i == predicted_max:
                res += 1
                predicted_max = maximum
        return res

        # Method 2 bfs 每一步都计算一遍下一步该怎么走
        # somewhat similar to greedy method
        # if len(nums) < 2: return 0
        # level, cur_max, maximum, i = 0, 0, 0, 0
        # while cur_max - i + 1 > 0:
        #     level += 1
        #     while i <= cur_max:
        #         maximum = max(maximum, i+nums[i])
        #         if maximum > len(nums)-2:
        #             return level
        #         i += 1
        #     cur_max = maximum

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 2 greedy
        res, predicted_max, maximum = 0, 0, 0
        for i in xrange(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if i == predicted_max:
                res += 1
                predicted_max = maximum
        return res

        # Approach 1 bfs
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

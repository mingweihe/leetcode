from random import randint


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # revervior sampling
        ans = -1
        cnt = 0
        for i, x in enumerate(self.nums):
            if x != target: continue
            if randint(0, cnt) == 0: ans = i
            cnt += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, acc = 0, 0
        mp = {0: -1}
        for i, x in enumerate(nums):
            acc += x
            target = acc - k
            if target in mp:
                res = max(res, i - mp[target])
            if acc not in mp:
                mp[acc] = i
        return res

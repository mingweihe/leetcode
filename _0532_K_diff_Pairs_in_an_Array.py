class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        d = {}
        res = 0
        if k == 0:
            for i in nums: d[i] = d.get(i, 0) + 1
            for i in d:
                if d[i] > 1: res += 1
            return res
        s = set(nums)
        for i in s: d[i] = 1
        for i in s:
            if d.get(i - k): res += 1
        return res

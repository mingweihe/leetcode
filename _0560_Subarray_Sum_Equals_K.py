class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, cnt, cur = 0, {0:1}, 0
        for x in nums:
            cur += x
            res += cnt.get(cur-k, 0)
            cnt[cur] = cnt.get(cur, 0) + 1
        return res

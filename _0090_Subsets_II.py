class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        time : O(2^n)
        space : O(n) n layers' stack space
        """
        nums.sort()
        res = []
        self.helper(res, [], nums, 0)
        return res

    def helper(self, res, cur, nums, start):
        res.append(list(cur))
        for i in xrange(start, len(nums)):
            if start != i and nums[i] == nums[i - 1]: continue
            cur.append(nums[i])
            self.helper(res, cur, nums, i + 1)
            cur.pop()

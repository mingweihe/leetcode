class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Approach 2 dfs/backtracking
        res = []
        def helper(cur, start):
            res.append(list(cur))
            for i in xrange(start, len(nums)):
                cur.append(nums[i])
                helper(cur, i+1)
                cur.pop()
        helper([], 0)
        return res
        # Approach bfs/interation
        # res = [[]]
        # for x in nums:
        #     for i in xrange(len(res)):
        #         res.append(res[i]+[x])
        # return res

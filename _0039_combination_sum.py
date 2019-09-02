class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        backtracking typical problem
        time : O(2^n)
        space : O(n)
        """
        res = []
        if not candidates: return res
        self.helper(res, [], candidates, target, 0)
        return res

    def helper(self, res, cur, candidates, target, start):
        if target < 0: return
        if target == 0: res.append(list(cur))
        for i in xrange(start, len(candidates)):
            cur.append(candidates[i])
            self.helper(res, cur, candidates, target - candidates[i], i)
            cur.pop()

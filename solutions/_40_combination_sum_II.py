class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not candidates: return res
        candidates.sort()
        self.helper(res, [], candidates, target, 0)
        return res

    def helper(self, res, cur, candidates, target, start):
        if target < 0: return
        if target == 0:
            res.append(list(cur))
            return
        for i in xrange(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1]: continue
            cur.append(candidates[i])
            self.helper(res, cur, candidates, target - candidates[i], i + 1)
            cur.pop()

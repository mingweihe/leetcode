class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0: return res
        self.helper(res, '', n, n)
        return res

    def helper(self, res, s, left, right):
        if left > right: return
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            self.helper(res, s + '(', left - 1, right)
        if right > 0:
            self.helper(res, s + ')', left, right - 1)

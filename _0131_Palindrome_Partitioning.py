class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
            backtracking algrithm
        """
        res = []
        self.helper(res, [], s)
        return res

    def helper(self, res, cur, s):
        if not s:
            res.append(list(cur))
            return
        for i in xrange(1, len(s) + 1):
            left = s[:i]
            if left == left[::-1]:
                cur.append(left)
                self.helper(res, cur, s[i:])
                cur.pop()

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.remove(s, res, 0, 0, ['(', ')'])
        return res

    def remove(self, s, ans, last_i, last_j, par):
        cnt = 0
        for i in xrange(last_i, len(s)):
            if s[i] == par[0]:
                cnt += 1
            elif s[i] == par[1]:
                cnt -= 1
            if cnt > -1: continue
            for j in xrange(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], ans, i, j, par)
            return
        s = s[::-1]
        if par[0] == '(':
            self.remove(s, ans, 0, 0, par[::-1])
        else:
            ans.append(s)

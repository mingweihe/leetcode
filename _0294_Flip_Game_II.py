class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
            keypoint: follow the natual way of playing the game
            backtracking approach
            time O(n!)
            space O(n!)
        """
        return self.helper(s, {})

    def helper(self, s, d):
        if s in d: return d[s]
        for i in xrange(len(s) - 1):
            if s[i] == s[i + 1] == '+':
                opponent = s[:i] + '--' + s[i + 2:]
                if not self.helper(opponent, d):
                    d[s] = True
                    return True
        d[s] = False
        return False

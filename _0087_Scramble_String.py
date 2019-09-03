class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        time O(n!)
        space O(n) -> n layers' stack space
        """
        if s1 == s2: return True
        L, letters = len(s1), [0] * 26
        for i in xrange(L):
            letters[ord(s1[i]) - 97] += 1
            letters[ord(s2[i]) - 97] -= 1
        for i in xrange(26):
            if letters[i] != 0:
                return False
        for i in xrange(1, L):
            if self.isScramble(s1[:i], s2[:i]) and \
                    self.isScramble(s1[i:], s2[i:]): return True
            if self.isScramble(s1[:i], s2[L - i:]) and \
                    self.isScramble(s1[i:], s2[:L - i]): return True
        return False

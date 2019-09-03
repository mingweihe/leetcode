class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        double array dp
        time O(n^2)
        space O(n^2)
        'abcba'
        0 1 2 1(3->0+1->1)
        a b c b             a
        """
        L = len(s)
        isPalindrome = [[0] * L for _ in xrange(L)]
        cuts = [0] * L
        for i in xrange(L):
            min_cut = i
            for j in xrange(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
                    min_cut = 0 if j == 0 else min(min_cut, cuts[j - 1] + 1)
            cuts[i] = min_cut
        return cuts[-1]

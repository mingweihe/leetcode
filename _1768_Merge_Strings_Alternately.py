class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Approach 2, two pointers
        i, j, m, n = 0, 0, len(word1), len(word2)
        res = ''
        while i < m or j < n:
            if i < m: res += word1[i]
            if j < n: res += word2[j]
            i, j = i+1, j+1
        return res
    
        ## Approach 1
        # m, n = len(word1), len(word2)
        # L = min(m, n)
        # res = ''
        # for i in xrange(L):
        #     res += word1[i]
        #     res += word2[i]
        # return res + word1[L:] + word2[L:]

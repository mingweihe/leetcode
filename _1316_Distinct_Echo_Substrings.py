class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        understanding the problem is the key to solution
        """
        # Approach 1 time O(n^2)  ~2700ms
        res = set()
        for i in xrange(2, len(text)+1, 2):
            for j in xrange(len(text)-i+1):
                if text[j:j+i/2] == text[j+i/2:j+i]:
                    res.add(text[j:j+i])
        return len(res)

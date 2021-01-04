class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        n/k 1
        1   0
        2   011
        3   0111001
        4   011100110110001
        """
        def invert(s):
            ans = [None] * len(s)
            for i, c in enumerate(s):
                if c == '0':
                    ans[i] = '1'
                else:
                    ans[i] = '0'
            return ''.join(ans)
        
        def dfs(i):
            if i == 1: return '0'
            si_1 = dfs(i-1)
            return si_1 + '1' + invert(si_1)[::-1]
        
        return dfs(n)[k-1]

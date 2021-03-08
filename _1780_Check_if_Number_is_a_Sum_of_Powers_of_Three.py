class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## Approach 2, O(log3(n))
        while n and n % 3 != 2:
            n /= 3
        return n % 3 != 2
            
        ## Approach 1, O(2^log3(n))
        # def dfs(idx, summ):
        #     if summ == n: return True
        #     if summ > n: return False
        #     cur = 3 ** idx
        #     if cur > n: return False
        #     if dfs(idx+1, summ) or dfs(idx+1, summ+cur): return True
        # return dfs(0, 0)

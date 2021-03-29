class Solution(object):
    def __init__(self):
        self.cache = dict()

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Approach 3, iteration, time: O(log(n))
        cnt = 0
        while n != 1:
            if n % 2 == 0: n >>= 1
            elif n == 3: n -= 1
            elif (n+1) % 4 == 0: n += 1
            else: n -= 1
            cnt += 1
        return cnt
    
        ##  Approach 2, recursion + memorization, time: O(log(n))
        # if n == 1: return 0
        # if n in self.cache: return self.cache[n]
        # ans = 1
        # if n % 2 == 0: ans += self.integerReplacement(n/2)
        # else: ans += min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        # self.cache[n] = ans
        # return ans
    
        ## Approach 1, recursion, time: around O(2^(log(n)/2))
        # if n == 1: return 0
        # if n % 2 == 0: return self.integerReplacement(n/2) + 1
        # return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))

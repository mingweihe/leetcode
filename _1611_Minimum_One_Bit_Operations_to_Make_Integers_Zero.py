from functools import lru_cache


class Solution:
    def minimumOneBitOperations(self, n):
        @lru_cache(None)
        def dfs(bits):
            if bits == '1': return 1
            if bits == '0': return 0
            if bits[0] == '0':
                return dfs(bits[1:])
            return helper(bits[1:]) + 1 + dfs('1' + '0' * (len(bits) - 2))
            
        @lru_cache(None)  
        def helper(bits):
            if bits == '1': return 0
            if bits == '0': return 1
            if bits[0] == '1':
                return dfs(bits[1:])
            return helper(bits[1:]) + 1 + dfs('1' + '0' * (len(bits) - 2))
            
        return dfs(bin(n)[2:])

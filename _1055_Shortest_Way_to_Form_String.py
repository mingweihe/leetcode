from collections import deque
import copy


class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        # Approach 2 time O(n) space O(n)
        # memorizing index with remained characters in source string
        M = len(source)
        memo = deque([[-1]*26])
        memo[-1][ord(source[-1])-97] = M-1
        for i in xrange(M-1, -1, -1):
            cur = copy.copy(memo[0])
            cur[ord(source[i])-97] = i
            memo.appendleft(cur)
        res, idx = 0, 0
        for c in target:
            if memo[0][ord(c)-97] == -1: return -1
            if memo[idx][ord(c)-97] == -1:
                res += 1
                idx = 0
            idx = memo[idx][ord(c)-97] + 1
            if idx == M:
                res += 1
                idx = 0
        return res + (idx != 0)
        
        # Approach 1 DP time O(m*n) space O(n)
        # dp = [float('inf')]*(len(target)+1)
        # dp[0] = 0
        # for i in xrange(1, len(target)+1):
        #     j, k = len(source)-1, i-1
        #     while j >= 0 and k >= 0:
        #         if source[j] == target[k]:
        #             if dp[k] != float('inf'):
        #                 dp[i] = min(dp[i], dp[k]+1)
        #             k -= 1
        #         j -= 1
        # return -1 if dp[-1] == float('inf') else dp[-1]

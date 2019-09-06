class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # Approach 2
        ls1, ls2 = len(s1), len(s2)
        nexts, dp = [0]*(ls2+1), [0]*(ls2+1)
        l, r = -1, -1
        for i in range(1, ls2+1):
            nexts[i], dp[i] = nexts[i-1], dp[i-1]
            for j in range(ls1):
                if s1[j] == s2[nexts[i]]:
                    nexts[i] = (nexts[i]+1)%ls2
                    if nexts[i] == 0: dp[i] += 1
            for k in range(i):
                if nexts[k] == nexts[i]:
                    l, r = k, i
                    break
            if l > -1: break
        if l > n1: return dp[n1]//n2
        return ((n1-l)//(r-l)*(dp[r]-dp[l])+dp[(n1-l)%(r-l)+l])//n2

        # Approach 1
        # i = j = cnts1 = cnts2 = 0
        # ls1, ls2 = len(s1), len(s2)
        # while cnts1 < n1:
        #     if s1[i] == s2[j]:
        #         j += 1
        #         if j == ls2:
        #             j = 0
        #             cnts2 += 1
        #     i += 1
        #     if i == ls1:
        #         i = 0
        #         cnts1 += 1
        # return cnts2 // n2

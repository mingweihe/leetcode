class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Method 4, Manacher's algorithm
        C = R = 0
        T = '#'.join('^{}$'.format(s))
        P = [0]*len(T)
        for i in xrange(2, len(T)-1):
            mirror = 2*C-i
            if i < R:
                P[i] = min(R-i, P[mirror])
            while T[i+P[i]+1] == T[i-(P[i]+1)]:
                P[i] += 1
            if P[i]+C > R:
                C = i
                R = P[i] + C
        max_len, center_index = max((x,i) for i,x in enumerate(P))
        return s[(center_index-max_len)/2:(center_index+max_len)/2]
        # Method 3
        # if s == s[::-1]: return s
        # start, max_len = 0, 1
        # for i in xrange(len(s)):
        #     if i-max_len > 0 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
        #         start = i-max_len-1
        #         max_len += 2
        #     elif i-max_len > -1 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
        #         start = i-max_len
        #         max_len += 1
        # return s[start:start+max_len]
        # Method 2
        # start, max_len = 0, 0
        # dp = [[False]*len(s) for i in xrange(len(s))]
        # for j in xrange(len(s)):
        #     for i in xrange(j+1):
        #         dp[i][j] = s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
        #         if dp[i][j]:
        #             cur_len = j-i+1
        #             if cur_len > max_len:
        #                 start, max_len = i, cur_len
        # return s[start:start+max_len]
        # Method 1
        # def extendAroundCenter(s, l, r):
        #     while l > -1 and r < len(s) and s[l] == s[r]:
        #         l, r = l-1, r+1
        #     cur_max = r-l-1
        #     if cur_max > self.max_length:
        #         self.start, self.max_length = l+1, cur_max
        # self.start = self.max_length = 0
        # for i in xrange(len(s)):
        #     extendAroundCenter(s, i, i)
        #     extendAroundCenter(s, i, i+1)
        # return s[self.start:self.start+self.max_length]

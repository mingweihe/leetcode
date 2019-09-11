class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 3 KMP
        r = s[::-1]
        nstr = s+'#'+r
        kmp = [0]*len(nstr)
        for i in xrange(1, len(nstr)):
            j = kmp[i-1]
            while j > 0 and nstr[i] != nstr[j]:
                j = kmp[j-1]
            if nstr[i] == nstr[j]:
                kmp[i] = j+1
        return r[:len(r)-kmp[-1]]+s

        # Approach 2 startswith O(n^2), while startswith is implemented in C
        # r = s[::-1]
        # for i in xrange(len(s)+1):
        #     if s.startswith(r[i:]):
        #         return r[:i] + s

        # Approach 1 time complexity(worst case) O(n^2), TLE
        # i, j, end = 0, len(s)-1, len(s)-1
        # while i < j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         i = 0
        #         end -= 1
        #         j = end
        # return s[end+1:][::-1] + s

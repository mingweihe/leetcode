class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Approach 2
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        reverse(0, len(s)-1)
        r = 0
        while r < len(s):
            l = r
            while r < len(s) and s[r] != ' ': r+=1
            reverse(l, r-1)
            r += 1
        # Approach 1
        # def reverse(left, right):
        #     while left < right:
        #         s[left], s[right] = s[right], s[left]
        #         left += 1
        #         right -= 1
        # reverse(0, len(s)-1)
        # start = 0
        # for i in xrange(len(s)):
        #     if s[i] == ' ':
        #         reverse(start, i-1)
        #         start = i + 1
        # reverse(start, len(s)-1)

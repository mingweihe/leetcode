class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def helper(x, y):
            left, right = 0, len(x) - 1
            while left < right and x[left] == y[right]:
                left += 1
                right -= 1
            s1 = x[left:right+1]
            s2 = y[left:right+1]
            return s1 == s1[::-1] or s2 == s2[::-1]
        return helper(a, b) or helper(b, a)

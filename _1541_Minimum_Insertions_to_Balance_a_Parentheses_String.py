class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        res = 0
        stack1 = stack2 = 0
        while i < n:
            while i < n and s[i] == '(':
                stack1 += 1
                i += 1
            while i < n and s[i] == ')':
                stack2 += 1
                i += 1
            while stack2:
                if stack1: stack1 -= 1
                else: res += 1
                stack2 -= 1
                if not stack2: res += 1
                else: stack2 -= 1
        return res + stack1 * 2

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {'(':')', '{':'}', '[':']'}
        for x in s:
            if x in dic:
                stack.append(x)
            elif not stack or dic[stack.pop()] != x:
                return False
        return not stack

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            stack.append(s[i])
            i += 1
            while i < len(s) and stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
                stack.pop()
                i += 1
        return ''.join(stack)

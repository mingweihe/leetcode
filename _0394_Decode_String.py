class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num = [['', 1]], ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                x, k = stack.pop()
                stack[-1][0] += x*k
            else:
                stack[-1][0] += c
        return stack[0][0]

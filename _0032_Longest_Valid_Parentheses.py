class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, stack, start = 0, [], -1
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - start)
                    else:
                        res = max(res, i - stack[-1])
        return res

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 2 stack
        # using last slot to maintain current last sequence
        stack = ['']
        for c in s:
            if c.isalpha():
                stack[-1] += c
            elif c == '(':
                stack.append('')
            else:
                # ss = stack.pop()[::-1]
                # stack[-1] += ss
                stack[-1] = stack[-2] + stack.pop()[::-1]
        return stack[0]

        # Approach 1 stack + an extra variable
        # using the extra variable to maintain last sequence
        # stack, cur = [], ''
        # for c in s:
        #     if c.isalpha(): cur += c
        #     elif c == '(':
        #         stack.append(cur)
        #         cur = ''
        #     else: cur = stack.pop() + cur[::-1]
        # return cur


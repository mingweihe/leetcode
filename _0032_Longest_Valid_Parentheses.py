class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Approach 3
        res = 0
        stack = [(')', -1)]
        for i, c in enumerate(s):
            if c == ')' and stack[-1][0] == '(':
                stack.pop()
                res = max(res, i-stack[-1][1])
            else:
                stack += (c, i),
        return res
    
        ## Approach 2
        # d = {0: -1}
        # stack = []
        # res = 0
        # for i, c in enumerate(s):
        #     if stack and stack[-1] == '(' and c == ')':
        #         d.pop(len(stack))
        #         stack.pop()
        #         res = max(res, i-d[len(stack)])
        #     else:
        #         stack += c,
        #         if len(stack) not in d:
        #             d[len(stack)] = i
        # return res
        
        ## Approach 1
        # res, stack, start = 0, [], -1
        # for i, x in enumerate(s):
        #     if x == '(':
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             start = i
        #         else:
        #             stack.pop()
        #             if not stack:
        #                 res = max(res, i - start)
        #             else:
        #                 res = max(res, i - stack[-1])
        # return res

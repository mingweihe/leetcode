class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Approach 2
        res = []
        cnt = 0
        for c in S:
            if c == '(' and cnt > 0: res.append(c)
            if c == ')' and cnt > 1: res.append(c)
            cnt += 1 if c == '(' else -1
        return ''.join(res)

        # Approach 1, inspired by valid parentheses
        # res = ''
        # stack = []
        # for x in S:
        #     if x == '(': stack.append(x)
        #     if len(stack) > 1: res += x
        #     if x == ')': stack.pop()
        # return res

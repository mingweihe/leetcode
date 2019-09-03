class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        typical stack quizz
        1. num accumulation
        2. stack stores sum/res between parentheses
        3. distinguish operations of += an =
        """
        res, sign, L, i = 0, 1, len(s), 0
        stack = []
        while i < L:
            if s[i].isdigit():
                num = int(s[i])
                while i+1 < L and s[i+1].isdigit():
                    i += 1
                    num = num*10 + int(s[i])
                res += num*sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif s[i] == ')':
                res = res*stack.pop() + stack.pop()
            i += 1
        return res

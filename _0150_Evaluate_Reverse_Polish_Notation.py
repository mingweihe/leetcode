class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
            1. pay attention to order of numbers popped from stack
            2. python / operation for negative / float number:
                -(-n1/n2) or int(float(n1) / n2)
        """
        if not tokens: return 0
        stack = []
        for x in tokens:
            if x.isdigit() or x[1:].isdigit():
                stack.append(int(x))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                cur = 0
                if x == '+': cur = n1 + n2
                elif x == '-': cur = n1 - n2
                elif x == '*': cur = n1*n2
                else: cur = int(float(n1)/n2)
                stack.append(cur)
        return stack[-1]

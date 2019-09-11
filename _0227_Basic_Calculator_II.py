class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 2
        stack, sign, num,  = [], '+', 0
        L, i = len(s), 0
        while i < L:
            c = s[i]
            if c.isdigit():
                num = int(c)
                while i+1 < L and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1
            if not c.isdigit() and c != ' ' or i == L-1:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*': stack.append(stack.pop()*num)
                else:
                    cur = stack.pop()
                    if cur < 0: stack.append(-(-cur/num))
                    else: stack.append(cur/num)
                sign = c
                num = 0
            i += 1
        return sum(stack)
        
        # Approach 1
        # return eval(s)

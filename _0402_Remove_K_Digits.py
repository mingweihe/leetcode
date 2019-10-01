class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
            solution: stack
        """
        L = len(num)
        if L == k: return '0'
        stack = []
        for i in xrange(L):
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        # zeros = 0
        # while zeros < len(stack) and stack[zeros] == '0': zeros += 1
        # if zeros == len(stack): return '0'
        # return ''.join(stack[zeros:])
        res = ''.join(stack).lstrip('0')
        return res if res else '0'

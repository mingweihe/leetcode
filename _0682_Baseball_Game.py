class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # Approach 1
        stack = []
        for x in ops:
            if x[-1].isdigit():
                stack.append(int(x))
            elif x == '+':
                stack.append(stack[-1]+stack[-2])
            elif x == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.pop()
        return sum(stack)
        # Approach 2
        # points = [0] * len(ops)
        # lastValRd = -1
        # for x in ops:
        #     if x[-1].isdigit():
        #         lastValRd += 1
        #         points[lastValRd] = int(x)
        #     elif x == 'D':
        #         lastValRd += 1
        #         points[lastValRd] = points[lastValRd - 1] * 2
        #     elif x == '+':
        #         lastValRd += 1
        #         points[lastValRd] = points[lastValRd - 1] + points[lastValRd - 2]
        #     else:
        #         points[lastValRd] = 0
        #         lastValRd -= 1
        # return sum(points)

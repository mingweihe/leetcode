class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # Approach 2 stack forward
        res, stack = [0] * len(T), []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res

        # Approach 1 stack backward
        # res, stack = [], []
        # for i in xrange(len(T)-1, -1, -1):
        #     while stack and T[i] >= T[stack[-1]]:
        #         stack.pop()
        #     if stack: res.append(stack[-1]-i)
        #     else: res.append(0)
        #     stack.append(i)
        # return res[::-1]

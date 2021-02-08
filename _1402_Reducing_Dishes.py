class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        # Approach 2, conciser
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res
    
        # Approach 1
        # satisfaction.sort()
        # res = 0
        # neg = []
        # pos = deque()
        # for x in satisfaction:
        #     if x < 0: neg += x,
        #     else: pos.append(x)
        # if not pos: return 0
        # res = sum(i * x for i, x in enumerate(pos, 1))
        # for i in xrange(len(neg)-1, -1, -1):
        #     pos.appendleft(neg[i])
        #     res = max(res, sum(i * x for i, x in enumerate(pos, 1)))
        # return res

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
            mathematical problem
            key point: you can always find a position if total > 0
                       first position is first summ greater than 0
        """
        total = summ = start = 0
        for i in xrange(len(gas)):
            cur = gas[i] - cost[i]
            total += cur
            if summ < 0:
                summ = cur
                start = i
            else: summ += cur
        return -1 if total < 0 else start

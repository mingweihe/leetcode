from collections import deque


class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        indices = [deque() for _ in xrange(10)]
        for i, c in enumerate(s):
            indices[int(c)].append(i)
        for x in t:
            num_t = int(x)
            if not indices[num_t]: return False
            for smaller_num in xrange(num_t):
                if indices[smaller_num] and indices[smaller_num][0] < indices[num_t][0]:
                    return False
            indices[num_t].popleft()
        return True

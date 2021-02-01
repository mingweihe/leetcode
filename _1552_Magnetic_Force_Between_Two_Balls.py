class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        l, r = 1, position[-1] - position[0]
        def valid(force):
            cnt = 0
            last = float('-inf')
            for pos in position:
                if pos - last >= force:
                    last = pos
                    cnt += 1
            return cnt >= m
        
        while l <= r:
            mid = l + (r-l) / 2
            if valid(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

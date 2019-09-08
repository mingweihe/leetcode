class Solution(object):
    def distanceBetweenBusStops(self, distance, s, d):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if s > d: s, d = d, s
        return min(sum(distance)-sum(distance[s:d]), sum(distance[s:d]))

class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        parent = {nex: arr[0] for arr in regions for nex in arr[1:]}
        seen = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            seen.add(region1)
        while region2 not in seen:
            region2 = parent[region2]
        return region2

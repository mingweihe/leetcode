class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        starts, ends = zip(*paths)
        return (set(ends) - set(starts)).pop()

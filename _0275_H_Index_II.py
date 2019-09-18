class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low, high = 0, len(citations)-1
        while low <= high:
            mid = (low + high) / 2
            target = len(citations) - mid
            if citations[mid] == target:
                return target
            elif citations[mid] > target:
                high = mid - 1
            else: low = mid + 1
        return len(citations) - low

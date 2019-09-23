import heapq


class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
            Huffman tree / coding algorithm
            It can make sure the minimum of a "coding" tree
        """
        heapq.heapify(blocks)
        while len(blocks) > 1:
            heapq.heappop(blocks)
            heapq.heappush(blocks, heapq.heappop(blocks)+split)
        return blocks[0]

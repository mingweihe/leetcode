class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Approach 2 O(n) Counting sort algorithm / thought
        cnt = [0] * len(citations)
        for x in citations:
            if x > len(citations): cnt[-1] += 1
            elif x > 0: cnt[x-1] += 1
        summ = 0
        for i in xrange(len(citations)-1, -1, -1):
            summ += cnt[i]
            if summ > i: return i+1
        return 0

        # Approach 1 O(n*log(n))
        # citations.sort(reverse=True)
        # for i,x in enumerate(citations):
        #     if x < i+1: return i
        # return len(citations)

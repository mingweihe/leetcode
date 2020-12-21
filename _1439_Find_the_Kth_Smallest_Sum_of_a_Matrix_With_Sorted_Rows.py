class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        ## Approach 2, sorting
        dp = [0]
        for row in mat:
            cur = []
            for a in row:
                for b in dp:
                    cur.append(a+b)
            cur.sort()
            dp = cur[:k]
        return dp[-1]

        ## Approach 1, heapq
        # hq = [0]
        # for row in mat:
        #     cur = []
        #     for a in row:
        #         for b in hq:
        #             heappush(cur, -(a-b))
        #             if len(cur) > k:
        #                 heappop(cur)
        #     hq = cur
        # return -hq[0]

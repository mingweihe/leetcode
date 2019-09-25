import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # Appraoch 2, time O(n*log(k))
        res, hq = [1], []
        for x in primes: heapq.heappush(hq, [x, 1, x])
        for i in xrange(1, n):
            res.append(hq[0][0])
            while hq[0][0] == res[-1]:
                nex = heapq.heappop(hq)
                nex[0] = res[nex[1]]*nex[2]
                nex[1] += 1
                heapq.heappush(hq, nex)
        return res[-1]

        # Approach 1, time O(n*k)
        # res = [0]*n
        # pos = [0]*len(primes)
        # nexts = [1]*len(primes)
        # nex = 1
        # for i in xrange(n):
        #     res[i] = nex
        #     nex = float('inf')
        #     for j in xrange(len(primes)):
        #         if nexts[j] == res[i]:
        #             nexts[j] = res[pos[j]]*primes[j]
        #             pos[j] += 1
        #         nex = min(nex, nexts[j])
        # return res[-1]

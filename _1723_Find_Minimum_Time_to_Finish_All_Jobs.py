class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
            key points1: how to represent the status of the subset of a problem
            key points2: how to do branch cutting
        """
        # ith job, from 0 to n-1, n is the end of the recursion to calculate the result
        def dfs(i):
            if i == len(jobs):
                self.res = min(self.res, max(workers))
                return
            seen = set()
            for j in xrange(k):
                if workers[j] in seen: continue
                seen.add(workers[j])
                if workers[j] + jobs[i] >= self.res: continue
                workers[j] += jobs[i]
                dfs(i + 1)
                workers[j] -= jobs[i]
        
        self.res = float('inf')
        workers = [0] * k
        dfs(0)
        return self.res

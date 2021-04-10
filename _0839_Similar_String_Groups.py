class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_similar(X, Y):
            cnt = 0
            for i in xrange(len(X)):
                if X[i] != Y[i]:
                    cnt += 1
                if cnt > 2: return False
            return True
        
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        
        roots = range(len(strs))
        for i in xrange(len(strs)-1):
            for j in xrange(1, len(strs)):
                if not is_similar(strs[i], strs[j]): continue
                ii, jj = find(i), find(j)
                if ii != jj: roots[ii] = roots[jj]
        return len(set([find(x) for x in roots]))

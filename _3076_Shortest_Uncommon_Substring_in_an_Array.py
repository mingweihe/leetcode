class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        cache = dict()
        def is_uncommon(idx, s):
            if ((idx, s) in cache): return cache[(idx, s)]
            for i, x in enumerate(arr):
                if i == idx: continue
                if s in x:
                    cache[(idx, s)] = False
                    return False
            cache[(idx, s)] = True
            return True
        
        res, n = [], len(arr)
        for j in xrange(n):
            cur = ""
            flag = False
            for l in xrange(1, len(arr[j])+1):
                if flag == True: break
                for k in xrange(len(arr[j])):
                    if cur != "":
                        flag = True
                    if is_uncommon(j, arr[j][k:k+l]):
                        if cur == "":
                            cur = arr[j][k:k+l]
                        else:
                            cur = min(cur, arr[j][k:k+l]) if len(cur) == len(arr[j][k:k+l]) else cur
            res += cur,
        return res

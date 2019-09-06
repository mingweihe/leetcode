class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # Approach 2
        check = set(A[0])
        res = [[c]*min(x.count(c) for x in A) for c in check]
        return [i for x in res for i in x]

        # Approach 1
        # res = collections.Counter(A[0])
        # for x in A[1:]: res &= collections.Counter(x)
        # return list(res.elements())

import collections


class Solution(object):
    def suggestedProducts(self, products, sw):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # Approach 2 TODO

        # Approach 1
        products.sort(reverse=True)
        dic = collections.defaultdict(collections.deque)
        for i in xrange(1, len(sw) + 1):
            for pro in products:
                if pro.startswith(sw[:i]):
                    dic[sw[:i]].append(pro)
                    if len(dic[sw[:i]]) > 3:
                        dic[sw[:i]].popleft()
        res = []
        for i in xrange(1, len(sw) + 1):
            res.append(reversed(dic[sw[:i]]))
        return res

import collections


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
            two pointers
            sliding window
            maining the max length of consecutive two
            while not focusing on the special start and end index.
            a little bit tricky
        """
        dic, i = collections.defaultdict(int), 0
        for j, v in enumerate(tree):
            dic[v] += 1
            if len(dic) > 2:
                dic[tree[i]] -= 1
                if dic[tree[i]] == 0: del dic[tree[i]]
                i += 1
        return j - i + 1

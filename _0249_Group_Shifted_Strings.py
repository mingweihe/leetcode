import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # Approach 2
        d = collections.defaultdict(list)
        for w in strings:
            key = []
            for i in xrange(1, len(w)):
                key.append((ord(w[i]) - ord(w[i - 1])) % 26)
            d[tuple(key)].append(w)
        return d.values()

        # Approach 1 return sorted sequences using bucket sort, could be a followed up
        # ignore this solution if only focusing on solving the puzzle
        # d = dict()
        # for w in strings:
        #     key = [0]
        #     for i in xrange(1, len(w)):
        #         key.append((ord(w[i])-ord(w[i-1])) % 26)
        #     key = tuple(key)
        #     if key not in d:
        #         d[key] = [[] for _ in xrange(26)]
        #     in_key = ord(w[0])-97
        #     d[key][in_key].append(w)
        # return [[w for ws in arr for w in ws] for arr in d.values()]

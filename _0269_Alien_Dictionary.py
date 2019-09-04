class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        key point:
        graph
        in degree
        create graph
        adjacency list
        topological sorting
        hashtable
        time complexity: O(V+E) or O(n*max(map(len, words)))
        space complexity: O(26) -> O(1)
        """
        res = ""
        degree = [0] * 26
        cnt = 0
        queue = []
        graph = dict()
        # initialize in degree, distinct letter count
        for w in words:
            for letter in w:
                key = ord(letter) - 97
                if degree[key] == 0:
                    cnt += 1
                    degree[key] = 1

        # create graph
        for i in xrange(len(words) - 1):
            cur = words[i]
            nex = words[i + 1]
            L = min(len(cur), len(nex))
            for j in xrange(L):
                if cur[j] != nex[j]:
                    if cur[j] not in graph:
                        graph[cur[j]] = set()
                    cur_adjacencies = graph[cur[j]]
                    if nex[j] not in cur_adjacencies:
                        cur_adjacencies.add(nex[j])
                        degree[ord(nex[j]) - 97] += 1
                    break

        # find verticle without 0 in degree, it's 1 in our logical
        for i, x in enumerate(degree):
            if x == 1: queue.append(chr(97 + i))

        # traverse graph
        while queue:
            c = queue.pop(0)
            res += c
            if c in graph:
                adj_list = graph.get(c)
                for x in adj_list:
                    key = ord(x) - 97
                    degree[key] -= 1
                    if degree[key] == 1:
                        queue.append(x)
        # if this is a cyclic graph, then no order exists
        if len(res) != cnt: return ""
        return res

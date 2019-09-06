# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Approach 2 BFS
        if not node: return node
        queue = [node]
        sets = set()
        while queue:
            nn = queue.pop(0)
            sets.add(nn)
            if nn.neighbors:
                for cur in nn.neighbors:
                    if cur not in sets:
                        queue.append(cur)
        dic = {}
        for x in sets:
            nn = Node(x.val, [])
            dic[x] = nn
        for x in sets:
            nn = dic[x]
            if x.neighbors:
                for xn in x.neighbors:
                    nn.neighbors.append(dic[xn])
        return dic[node]

        # Approach 1 DFS
        # return self.helper(node, {})

    # def helper(self, node, maps):
    #     if not node: return node
    #     if node in maps: return maps[node]
    #     nn = Node(node.val, [])
    #     maps[node] = nn
    #     if node.neighbors:
    #         for x in node.neighbors:
    #             nn.neighbors.append(self.helper(x, maps))
    #     return nn
        # Approach 3
        # return copy.deepcopy(node)

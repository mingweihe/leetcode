# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Approach 2 map
        maps = dict()
        node = head
        while node:
            maps[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            maps[node].next = maps.get(node.next)
            maps[node].random = maps.get(node.random)
            node = node.next
        return maps.get(head)

        # Approach 2 1-1'-2-2'-3-3'

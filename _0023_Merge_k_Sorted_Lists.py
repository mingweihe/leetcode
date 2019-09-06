from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Approach 2, n*log(k) [n=number of all nodes in lists]
        cur_node = dummy = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val, node))
        while q.qsize():
            cur_node.next = q.get()[1]
            cur_node = cur_node.next
            if cur_node.next:
                q.put((cur_node.next.val, cur_node.next))
        return dummy.next

        # Approach 1 k*n [n=average length of nodes in lists]
        # sentinel = ListNode(0)
        # cur_node = sentinel
        # while True:
        #     cur_min_node = None
        #     cur_min_i = -1
        #     for i, node in enumerate(lists):
        #         if node and (not cur_min_node or node.val < cur_min_node.val):
        #             cur_min_node = node
        #             cur_min_i = i
        #     if cur_min_node:
        #         lists[cur_min_i] =  cur_min_node.next
        #         cur_node.next = cur_min_node
        #         cur_node = cur_node.next
        #     else:
        #         break
        # return sentinel.next

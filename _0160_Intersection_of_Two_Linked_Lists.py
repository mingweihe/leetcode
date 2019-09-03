# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        # Approach 1
        # dic, a, b = {}, headA, headB
        # while a:
        #     dic[a] = a.val
        #     a = a.next
        # while b:
        #     if b in dic: return b
        #     b = b.next
        # Approach 2
        la, lb, a, b = 0, 0, headA, headB
        while a:
            la += 1
            a = a.next
        while b:
            lb += 1
            b = b.next
        diff = la - lb
        a, b = headA, headB
        if diff > 0:
            while diff:
                a = a.next
                diff -= 1
        else:
            while diff:
                b = b.next
                diff += 1
        while a:
            if a is b: return a
            a, b = a.next, b.next

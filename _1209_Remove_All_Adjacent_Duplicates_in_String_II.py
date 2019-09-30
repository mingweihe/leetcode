# self defined class for doubly linked list solution
class Node(object):
    def __init__(self, letter, num):
        self.letter = letter
        self.num = num
        self.next = None
        self.prev = None


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Approach 3 stack, clean and conciser
        stack = [['#', 0]]
        for i in xrange(len(s)):
            if stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k: stack.pop()
            else:
                stack.append([s[i], 1])
        return ''.join(c * n for c, n in stack)

        # Approach 2 stack
#         stack, L = [[s[0], 1]], len(s)
#         for i in xrange(1, L):
#             if stack and stack[-1][0] == s[i]: stack[-1][1] += 1
#             else: stack.append([s[i], 1])
#             while stack and stack[-1][1] % k == 0:
#                 stack.pop()
#             if stack: stack[-1][1] %= k
#         return ''.join(c*n for c, n in stack)

        # Approach 1 doubly linked list
#         dummy = Node('', 0)
#         dummy.next = node = self.create_dlink(s)
#         node.prev = dummy
#         while node and node.num != 0:
#             if node.num % k == 0:
#                 if node.prev.letter != node.next.letter:
#                     node.prev.next = node.next
#                     node.next.prev = node.prev
#                     node = node.next
#                 else:
#                     node.prev.num += node.next.num
#                     node.prev.next = node.next.next
#                     node.next.next.prev = node.prev
#                     node = node.prev
#             elif node.num < k:
#                 node = node.next
#             else:
#                 node.num %= k
#                 node = node.next
#         return self.create_string(dummy.next)

#     def create_dlink(self, s):
#         node = head = Node(s[0], 1)
#         L = len(s)
#         for i in xrange(1, L):
#             if s[i] == s[i-1]:
#                 node.num += 1
#             else:
#                 node.next = Node(s[i], 1)
#                 node.next.prev = node
#                 node = node.next
#         node.next = Node('', 0)
#         node.next.prev = node
#         return head

#     def create_string(self, dl):
#         res = ''
#         while dl:
#             res += dl.letter*dl.num
#             dl = dl.next
#         return res

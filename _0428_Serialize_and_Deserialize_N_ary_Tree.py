"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        def helper(node):
            if not node: return
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for _ in node.children:
                helper(_)
        helper(root)
        return ','.join(res)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        def helper(A):
            val = int(A.popleft())
            size = int(A.popleft())
            node = Node(val)
            node.children = [helper(A) for _ in range(size)]
            return node
        return helper(deque(data.split(',')))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

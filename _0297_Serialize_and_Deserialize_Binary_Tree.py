# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def do_serialize(node):
            if node:
                vals.append(str(node.val))
                do_serialize(node.left)
                do_serialize(node.right)
            else:
                vals.append('#')

        vals = []
        do_serialize(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def do_deserialize():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = do_deserialize()
            node.right = do_deserialize()
            return node

        vals = iter(data.split(','))
        return do_deserialize()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

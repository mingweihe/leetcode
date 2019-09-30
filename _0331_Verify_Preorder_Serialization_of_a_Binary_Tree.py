class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        In short, this is a checking number of hashtag(#) problem, because only hashtag(#) and numbers exist.
        We have the following constraints for pre-order traversal of a binary tree:
        1. For any tree, number of nodes == number of edges + 1, (so we add 1 to number of edges first)
        2. The hashtag(#) should only appear when there's edge available.
        Then we have the algorithm or statement:
        1. each node consumes 1 edge
        2. each non-leaf node creates two edges
        3. whenever edges are smaller than 0, return false, which means number of hashtag(#) is too much
        4. Finally, edges should be zero to meet the 1st constraint which is number of nodes == number of edges + 1
        """
        nodes, edges = preorder.split(','), 1
        for node in nodes:
            edges -= 1
            if edges < 0: return False
            if node != '#': edges += 2
        return edges == 0

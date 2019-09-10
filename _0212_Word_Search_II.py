class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.word = None


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        trie = self.buildTrie(words)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, trie, res)
        return res

    def dfs(self, board, i, j, trie, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
        letter = board[i][j]
        if letter == '#': return
        nextTrie = trie.children[ord(letter) - 97]
        if nextTrie is None: return
        if nextTrie.word is not None:
            res.append(nextTrie.word)
            nextTrie.word = None
        board[i][j] = '#'
        self.dfs(board, i, j + 1, nextTrie, res)
        self.dfs(board, i, j - 1, nextTrie, res)
        self.dfs(board, i + 1, j, nextTrie, res)
        self.dfs(board, i - 1, j, nextTrie, res)
        board[i][j] = letter

    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                index = ord(c) - 97
                if node.children[index] is None:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.word = word
        return root

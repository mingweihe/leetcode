class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
            trie solution
            implemented by dictionary
        """
        self.root = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def _search(_node, _word):
            for i, c in enumerate(_word):
                if c != '.':
                    _node = _node.get(c)
                    if not _node: return False
                else:
                    return any(_search(n, _word[i + 1:]) for n in _node.values() if n)
            if '$' in _node: return True
            return False

        return _search(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

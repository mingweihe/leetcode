class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.data = None
        self.hotness = 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.typed = ''
        for i, sen in enumerate(sentences):
            self.add_sentence(sen, times[i])

    def add_sentence(self, sen, hot):
        trie = self.root
        for c in sen:
            if c not in trie.children: trie.children[c] = TrieNode()
            trie = trie.children[c]
        trie.data = sen
        trie.hotness -= hot

    def dfs(self, trie):
        ans = []
        if not trie: return ans
        if trie.data: ans += (trie.hotness, trie.data),
        for sub_trie in trie.children.values():
            ans += self.dfs(sub_trie)
        return ans

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.add_sentence(self.typed, 1)
            self.typed = ''
            return []
        sen = self.typed = self.typed + c
        trie = self.root
        for c in sen:
            if c not in trie.children: return []
            trie = trie.children[c]
        return [s for _, s in sorted(self.dfs(trie))[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

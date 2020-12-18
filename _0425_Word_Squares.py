class Node:
    def __init__(self):
        self.children = {}
        self.words = []

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        root = Node()
        def add(word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
                cur.words += word,
        
        ans = []
        for word in words:
            add(word)
        
        def get_words(pre):
            cur = root
            for c in pre:
                if c not in cur.children:
                    return []
                cur = cur.children[c]
            return cur.words
        
        def backtracking(idx, ws):
            if idx == len(ws[0]):
                ans.append(ws[:])
                return
            
            pref = [_[idx] for _ in ws]
            for word in get_words(pref):
                ws += word,
                backtracking(idx+1, ws)
                ws.pop()
            
        for word in words:
            backtracking(1, [word])
            
        return ans

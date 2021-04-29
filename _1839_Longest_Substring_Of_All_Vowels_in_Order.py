class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        d = {'a': [-1, -1], 'e': [-1, -1], 'i': [-1, -1], 'o': [-1, -1], 'u': [-1, -1]}
        ans = 0
        keys = 'aeiou'
        d[word[0]][0] = d[word[0]][1] = 0
        st = set([word[0]])
        for i in xrange(1, len(word)):
            st.add(word[i])
            if word[i] == word[i-1]:
                d[word[i]][1] = i
            else:
                d[word[i]][0] = d[word[i]][1] = i
            flag = True
            for k in xrange(1, 5):
                if d[keys[k-1]][1] != d[keys[k]][0] - 1:
                    flag = False
                    break
            if not flag: continue
            ans = max(ans, i - d['a'][0] + 1)
        return ans

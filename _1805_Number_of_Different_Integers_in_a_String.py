class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        st = set()
        cur = ''
        for x in word+'a':
            if x.isdigit():
                cur += x
            elif cur:
                st.add(int(cur))
                cur = ''
        return len(st)

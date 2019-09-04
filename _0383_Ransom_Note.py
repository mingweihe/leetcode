class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Approach 1
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i): return False
        return True
        # Approach 2
        # d = {}
        # for i in magazine:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # for i in ransomNote:
        #     if i in d:
        #         if d[i] == 0:
        #             return False
        #         else:
        #             d[i] -= 1
        #     else:
        #         return False
        # return True

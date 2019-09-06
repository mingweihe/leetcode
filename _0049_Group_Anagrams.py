class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Approach 2
        dic = {}
        for x in strs:
            key = tuple(sorted(x))
            dic[key] = dic.get(key, []) + [x]
        return dic.values()

        # Approach 1
        # dic = collections.defaultdict(list)
        # for x in strs:
        #     cnt = [0]*26
        #     for i in x: cnt[ord(i)-97] += 1
        #     s = ''
        #     for i in cnt: s+=str(i)+chr(i+97)
        #     dic[s].append(x)
        # return dic.values()

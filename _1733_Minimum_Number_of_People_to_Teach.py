class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        def helper(lang_idx):
            ans = set()
            for u, v in todo_f:
                u_lang = languages[u-1]
                v_lang = languages[v-1]
                if lang_idx not in u_lang:
                    ans.add(u)
                if lang_idx not in v_lang:
                    ans.add(v)
            return len(ans)
            
        languages = map(set, languages)
        todo_f = []
        for u, v in friendships:
            if not set(languages[u-1]) & set(languages[v-1]):
                todo_f += [u, v],
        
        res = float('inf')
        for i in xrange(1, n+1):
            res = min(res, helper(i))
        return res

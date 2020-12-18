from heapq import heappush, heappop


class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        Tricky is if one's creatively to write many utility functions
        """
        def generate_abbrs(s):
            hq = []
            def dfs(idx, cur, cnt):
                if idx == len(s):
                    ans = cur + (str(cnt) if cnt else '')
                    heappush(hq, (len(ans), ans))
                    return
                if cnt > 0: dfs(idx+1, cur+str(cnt)+s[idx], 0)
                else: dfs(idx+1, cur+s[idx], 0)
                dfs(idx+1, cur, cnt+1)
            dfs(0, '', 0)
            return hq
        

        def is_valid(s):
            def is_one_of_the_abbr(_s, _abbr):
                i, j = 0, 0
                while i < len(_s):
                    if _abbr[j].isalpha():
                        if _s[i] != _abbr[j]: return False
                        i += 1
                        j += 1
                    else:
                        start = j
                        while j < len(_abbr) and _abbr[j].isdigit():
                            j += 1
                        i += int(_abbr[start:j])
                return True
            
            return all([not is_one_of_the_abbr(x, s) for x in dictionary])
        
        dictionary = [x for x in dictionary if len(x) == len(target)]
        target_abbrs = generate_abbrs(target)
        
        while target_abbrs:
            _, abbr = heappop(target_abbrs)
            if is_valid(abbr): return abbr
        return ''

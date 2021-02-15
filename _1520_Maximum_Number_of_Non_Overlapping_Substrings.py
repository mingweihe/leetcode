class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
            greedy + key ranges calculation
        """
        ranges = dict()
        for i, c in enumerate(s):
            if c not in ranges: ranges[c] = [i, i]
            else: ranges[c][1] = i
        
        for k, (start, end) in ranges.items():
            stack = [(start, end)]
            while stack:
                s1, e1 = stack.pop()
                for i in xrange(s1, e1+1):
                    new_s, new_e = ranges[s[i]]
                    if new_s < start:
                        stack.append((new_s, start-1))
                        start = new_s
                    if new_e > end:
                        stack.append((end+1, new_e))
                        end = new_e
            ranges[k] = [start, end]
        
        res = []
        seen_ranges = []
        sorted_ranges = sorted(ranges.values(), key=lambda x: x[1]-x[0])
        for start, end in sorted_ranges:
            if any(start <= e1 and end >= s1 for s1, e1 in seen_ranges): continue
            seen_ranges += [start, end],
            res += s[start:end+1],
        return res

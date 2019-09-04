class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # Approach 2
        d = {}
        for x in cpdomains:
            cnt, domain = x.split()
            cnt = int(cnt)
            subs = domain.split('.')
            cur = ''
            for sub in subs[::-1]:
                if not cur:
                    cur = sub
                else:
                    cur = sub + '.' + cur
                d[cur] = d.get(cur, 0) + cnt
        return ['%d %s' % (v, k) for k, v in d.items()]
        # Approach 1
        # d = collections.Counter()
        # for x in cpdomains:
        #     cnt, domain = x.split()
        #     d[domain] += int(cnt)
        #     for i in range(len(domain)):
        #         if domain[i] == '.':
        #             d[domain[i+1:]] += int(cnt)
        # return ['%d %s' % (v, k) for k,v in d.items()]

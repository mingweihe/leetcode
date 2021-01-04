class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        rank = dict()
        for vote in votes:
            for i, x in enumerate(vote):
                if x not in rank:
                    rank[x] = [0] * len(vote)
                rank[x][i] += 1
        res = sorted(rank.items(), key=lambda x: [map(lambda k: -k, x[1]), x[0]])
        return ''.join(zip(*res)[0])

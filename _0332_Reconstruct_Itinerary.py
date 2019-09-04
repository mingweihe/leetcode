import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        routes = []
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            # comma , here equals [b]
            targets[a] += b,
            
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            routes.append(airport)
        visit('JFK')
        return routes[::-1]

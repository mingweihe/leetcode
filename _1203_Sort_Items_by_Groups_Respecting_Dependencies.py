from collections import defaultdict
from collections import deque


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        g2is = defaultdict(list)
        g2gs = defaultdict(set)
        i2is = defaultdict(list)
        g_in_degree = defaultdict(int)
        i_in_degree = defaultdict(int)
        min_group = m
        # build group to items map
        for i, g in enumerate(group):
            if g == -1:
                group[i] = min_group
                min_group += 1
            g2is[group[i]].append(i)
        # build groups and items in-degrees, group and items graphs
        for i_to, i_froms in enumerate(beforeItems):
            group_to = group[i_to]
            for i_from in i_froms:
                group_from = group[i_from]
                if group_to != group_from:
                    # make sure no duplicate dependecies
                    if group_to not in g2gs[group_from]:
                        g2gs[group_from].add(group_to)
                        g_in_degree[group_to] += 1
                else:
                    i2is[i_from].append(i_to)
                    i_in_degree[i_to] += 1
        # create ordered group list and check conflicts
        group_ans, dq = [], deque()
        for i in xrange(min_group):
            if g_in_degree[i] == 0:
                group_ans.append(i)
                dq.append(i)
        while dq:
            g_id = dq.popleft()
            for next_g_id in g2gs[g_id]:
                g_in_degree[next_g_id] -= 1
                if g_in_degree[next_g_id] == 0:
                    dq.append(next_g_id)
                    group_ans.append(next_g_id)
        if len(group_ans) != min_group: return []
        # create final ordered items list and check conflicts
        res = []
        for g_id in group_ans:
            dq, num_items = deque(), 0
            for i in g2is[g_id]:
                if i_in_degree[i] == 0:
                    num_items += 1
                    res.append(i)
                    dq.append(i)
            while dq:
                i = dq.popleft()
                for next_item in i2is[i]:
                    i_in_degree[next_item] -= 1
                    if i_in_degree[next_item] == 0:
                        num_items += 1
                        dq.append(next_item)
                        res.append(next_item)
            if num_items != len(g2is[g_id]): return []
        return res

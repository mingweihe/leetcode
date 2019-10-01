import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
            shortest path problem
        """
        # Approach 3 Heap time O(E*log(E))
        hq = [[0, K]]
        graph = collections.defaultdict(list)
        pathes = {}
        for u, v, w in times: graph[u].append([v, w])
        while hq:
            dis, node = heapq.heappop(hq)
            if node not in pathes:
                pathes[node] = dis
                for v, w in graph[node]:
                    heapq.heappush(hq, [w + dis, v])
        return max(pathes.values()) if len(pathes) == N else -1

        # Approach 2 Queue time O(V+E) to O(V*E)
        # dq = collections.deque([[K, 0]])
        # graph = collections.defaultdict(list)
        # dists = [0]+[float('inf')]*N
        # for u, v, w in times: graph[u].append([v, w])
        # while dq:
        #     node, dis = dq.popleft()
        #     if dis < dists[node]:
        #         dists[node] = dis
        #         for v, w in graph[node]:
        #             dq.append([v, w+dis])
        # res = max(dists)
        # return res if res != float('inf') else -1

        # Approach 1 bellman-ford time O(N*E)
        # nodes = [float('inf')]*N
        # nodes[K-1] = 0
        # for i in xrange(N):
        #     for u, v, w in times:
        #         nodes[v-1] = min(nodes[v-1], nodes[u-1]+w)
        # longest_dist = max(nodes)
        # return -1 if longest_dist == float('inf') else longest_dist

'''

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

'''

from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        map = defaultdict(list)
        for [n1, n2] in connections:
            map[n1].append(n2)
            map[n2].append(n1)

        visited = defaultdict(lambda: False)
        # node with lowest index that this node can reach
        lowestNode = defaultdict(lambda: float('-inf'))
        # time that dfs went through this node, or depth in DFS
        discoverTime = defaultdict(lambda: float('-inf'))

        parentMap = defaultdict(lambda: -1)
        results = []

        def dfs(node, time):
            if visited[node]: return
            visited[node] = True
            lowestNode[node] = time
            discoverTime[node] = time

            for t in map[node]:
                # dfs over all adjacent nodes
                if not visited[t]:
                    parentMap[t] = node
                    dfs(t, time + 1)
                    lowestNode[node] = min(lowestNode[t], lowestNode[node])

                    if lowestNode[t] > discoverTime[node]:
                        results.append([node, t])
                else:
                    if t != parentMap[node]:
                        lowestNode[node] = min(lowestNode[node], discoverTime[t])

        dfs(0, 0)
        return results




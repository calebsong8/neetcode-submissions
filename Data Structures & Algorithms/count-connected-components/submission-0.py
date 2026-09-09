class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # pattern: undirected graph
        # trigger: undirected graph
        # return int of connected component

        visited = set()

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            if node in visited:
                return
            
            visited.add(node)
            
            for nei in adj[node]:
                if nei != par:
                    dfs(nei, node)
            return True
        
        connectedCount = 0
        for i in range(n):
            if dfs(i, i-1):
                connectedCount+=1;
        
        return connectedCount;
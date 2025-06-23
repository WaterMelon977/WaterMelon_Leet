class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        D=defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        

        
        seen=set()
        seen.add(source)
        def dfs(node):
            if node == destination: 
                return True
            for nbr in D[node]:
                if nbr not in seen:
                    seen.add(nbr)
                    if dfs(nbr):
                        return True
            return False

        return dfs(source)
        
        # Time: O(N + E), Space: O(N + E)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        seen.add(source)
        stack = [source]
 
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        
        return False

        
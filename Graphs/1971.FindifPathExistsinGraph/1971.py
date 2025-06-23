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
        
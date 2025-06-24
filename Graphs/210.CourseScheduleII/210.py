class Solution:
    def findOrder(self, numCourses: int, p: List[List[int]]) -> List[int]:
        D=defaultdict(list)
        
        for u,v in p:
            D[u].append(v)

        UNVISITED=0
        VISITING=1
        VISITED=2
        ans=[]

        trav=[0]*(numCourses)

        def dfs(source):
            if trav[source]== 2:
                return True
            elif trav[source] ==1:  
                return False
            else:
                trav[source] =1
                
                for node in D[source]:
                    if not dfs(node):
                        return False
                        
                
                    
                trav[source]=2
                ans.append(source)
                return True
                

        for i in range(numCourses):
            if dfs(i) == False: 
                return []
        return ans
        
# Time: O(V + E), Space: O(V + E)
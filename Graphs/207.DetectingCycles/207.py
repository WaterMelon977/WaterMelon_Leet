class Solution:
    def canFinish(self, numCourses: int, p: List[List[int]]) -> bool:
        D=defaultdict(list)
        
        for u,v in p:
            D[u].append(v)

        UNVISITED=0
        VISITING=1
        VISITED=2

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
                return True
                

        for i in range(numCourses):
            if dfs(i) == False: 
                return False
        return True 


class Solution:
    def canFinish(self, numCourses: int, p: List[List[int]]) -> bool:
        D=defaultdict(list)
        
        for u,v in p:
            D[u].append(v)

        UNVISITED=0
        VISITING=1
        VISITED=2

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
                return True
                

        for i in range(numCourses):
            if dfs(i) == False: 
                return False
        return True 

# Time Complexity: O(N + E) 
# Space Complexity: O(N + E)

        
        
        


        
        
        
        
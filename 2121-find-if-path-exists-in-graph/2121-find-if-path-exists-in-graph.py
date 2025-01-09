class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        lib = defaultdict(list)

        for u,v in edges: 
            lib[v].append(u)
            lib[u].append(v)
        seen = set()
        final = [False]

        def dfs(node):
            if node == destination:
                final[0] = True  
                return  
            for nn in lib[node]:
                if final[0] == True: 
                    return 
                if nn not in seen:
                    seen.add(node)
                    dfs(nn)
                
            return False 
            
            
              
        dfs(source)
        return final[0]

    
            

        
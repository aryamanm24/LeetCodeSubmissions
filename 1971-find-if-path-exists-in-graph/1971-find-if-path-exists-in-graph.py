from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Trivial case
        if(source == destination):
            return True
        
        # Build adj. list from edges list
        adjl = {}

        for edge in edges:
            if(edge[0] not in adjl):
                adjl[edge[0]] = [edge[1]]
            else:
                adjl[edge[0]].append(edge[1])
            
            if(edge[1] not in adjl):
                adjl[edge[1]] = [edge[0]]
            else:
                adjl[edge[1]].append(edge[0])
        
        # Now BFS
        queue = deque([source])
        visited = {source}

        while(queue):
            node = queue.popleft()

            if(node == destination):
                return True
            
            for neighbour in adjl[node]:
                if(neighbour not in visited):
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        return False
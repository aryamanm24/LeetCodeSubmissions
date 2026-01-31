class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        length = len(candidates)
        result = []

        def dfs(start_index: int, path: List[int], target: int) -> None:

            # Invalid case:
            if(target < 0):
                return
            
            # Valid case:
            if(target == 0):
                result.append(path[:])
                return
            
            for i in range(start_index, length):
                
                if(i > start_index and candidates[i] == candidates[i-1]):
                    continue

                path.append(candidates[i])
                dfs(i+1, path, target-candidates[i])
                path.pop()
        
        
        dfs(0, [], target)
        return result
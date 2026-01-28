class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # backtracking method
        result = []

        def dfs(start: int, path: List[int]) -> None:

            # base case (limiting):
            if(len(path) == k):
                result.append(path[:]) # Append result's copy to the main array
                return

            for num in range(start, n+1):
                path.append(num)
                dfs(num+1, path)
                path.pop()


        dfs(1, [])
        return result
        
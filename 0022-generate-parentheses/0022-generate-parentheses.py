class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def dfs(closed_count: int, open_count:int, curr_brackets: str) -> None:

            # limiting base case: length of brackets = 2*n
            if(len(curr_brackets) == 2*n):
                # Append to result and return
                result.append(curr_brackets)
                return
            
            if(open_count < n):
                dfs(closed_count, open_count+1, curr_brackets+"(")
            if(closed_count < open_count):
                dfs(closed_count + 1, open_count, curr_brackets + ")")


        dfs(0, 0, "")
        return result 
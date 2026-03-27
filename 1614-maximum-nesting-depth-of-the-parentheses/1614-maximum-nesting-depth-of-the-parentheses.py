class Solution:
    def maxDepth(self, s: str) -> int:
        
        curr_depth = 0
        max_depth = 0

        for char in s:
            if(char == '('):
                curr_depth += 1
            elif(char == ')'):
                curr_depth -= 1
            
            max_depth = max(max_depth, curr_depth)
        
        return max_depth
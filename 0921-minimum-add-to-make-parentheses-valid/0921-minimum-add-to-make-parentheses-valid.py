class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        for char in s:
            if(char == '('):
                stack.append(char)
            else:
                if(not stack):
                    stack.append(char)
                elif(stack[-1] == '('):
                    stack.pop()
                elif(stack[-1] == ')'):
                    stack.append(char)
        
        return len(stack)
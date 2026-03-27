class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        length = len(s)
        stack = [] # store indices?

        for i in range(length):
            if(s[i] == '('):
                stack.append(i)
            elif(s[i] == ')'):
                if(stack and s[stack[-1]] == '('):
                    stack.pop()
                else:
                    stack.append(i)
            
        
        # Now rebuild the new string, skipping the indices
        # which are not to be considered

        bad = set(stack) # Converting for O(1) lookup
        result = []

        for i, char in enumerate(s):
            if(i not in bad):
                result.append(char)
        
        return "".join(result)
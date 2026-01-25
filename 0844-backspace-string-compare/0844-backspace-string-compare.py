class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s = []
        stack_t = []

        # Edge case to consider: if the stack is already empty, then backspacing more will just
        # result in the stack still being empty

        for char1 in s:
            if(char1 == '#' and len(stack_s) > 0):
                stack_s.pop()
            elif(char1 == '#' and len(stack_s) == 0): # Edge case
                continue
            else:
                stack_s.append(char1)
        
        for char2 in t:
            if(char2 == '#' and len(stack_t) > 0):
                stack_t.pop()
            elif(char2 == '#' and len(stack_t) == 0): # Edge case
                continue
            else:
                stack_t.append(char2)
        
        string_s = "".join(stack_s)
        string_t = "".join(stack_t)

        return string_s == string_t
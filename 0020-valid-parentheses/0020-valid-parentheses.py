class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brackets_set = ['(', '{', '[']

        stack = []

        for bracket in s:
            if(bracket in open_brackets_set):
                stack.append(bracket)
            else:
                if(bracket == ')' and stack and stack[-1] == '('):
                    stack.pop()
                elif(bracket == '}' and stack and stack[-1] == '{'):
                    stack.pop()
                elif(bracket == ']' and stack and stack[-1] == '['):
                    stack.pop()
                else:
                    stack.append(bracket)
            
        return len(stack)==0
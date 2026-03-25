class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ['(', '{', '['] # Fixed length
        stack = []

        for char in s:
            if(char in opening): # 3n
                stack.append(char)
            
            else:
                if(char == ')'):
                    if(stack and stack[-1] == '('):
                        stack.pop()
                    else:
                        stack.append(char)
                elif(char == '}'):
                    if(stack and stack[-1] == '{'):
                        stack.pop()
                    else:
                        stack.append(char)
                elif(char == ']'):
                    if(stack and stack[-1] == '['):
                        stack.pop()
                    else:
                        stack.append(char)
            
        return len(stack) == 0
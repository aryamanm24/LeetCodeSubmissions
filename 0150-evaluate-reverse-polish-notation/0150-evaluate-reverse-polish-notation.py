class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Stack
        stack = []

        for token in tokens:

            if token.lstrip('-').isdigit():
                stack.append(int(token))
            
            else:
                if(len(stack) < 2):
                    return float('-inf')
                
                b = int(stack.pop())
                a = int(stack.pop())

                if(token == '+'):
                    stack.append(a + b)
                elif(token == '-'):
                    stack.append(a - b)
                elif(token == '*'):
                    stack.append(a * b)
                elif(token == '/'):
                    stack.append(int(a/b))
        
        return stack[-1]

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        current_string = ""
        current_num = 0

        for char in s:

            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Handle multi-digit
            
            elif char == '[':
                # Save state and reset
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            
            elif char == ']':
                # Pop and combine
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            
            else:  # letter
                current_string += char

        return  current_string

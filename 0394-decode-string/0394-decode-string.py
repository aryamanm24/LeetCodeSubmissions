class Solution:
    def decodeString(self, s: str) -> str:
        
        string_stack = []
        number_stack = []

        curr_string = ""
        curr_num = 0

        for char in s:

            if(char.isdigit()):
                curr_num = (curr_num)*10 + int(char)
            
            # save progress
            elif(char == '['):
                string_stack.append(curr_string)
                number_stack.append(curr_num)
                curr_num = 0
                curr_string = ""
            
            elif(char == ']'):
                repeat_count = number_stack.pop()
                prev_string = string_stack.pop()
                curr_string = prev_string + (curr_string * repeat_count)
            else:
                curr_string += char
        
        return curr_string

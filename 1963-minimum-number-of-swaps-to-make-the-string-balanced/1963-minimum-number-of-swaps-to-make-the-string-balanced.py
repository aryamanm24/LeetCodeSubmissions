import math

class Solution:
    def minSwaps(self, s: str) -> int:
        
        stack = [] # keep count of unmatched [
        
        for char in s:
            if(char == '['):
                stack.append(char)
            elif(stack and char == ']' and stack[-1]=='['):
                stack.pop()
        
        return math.ceil(len(stack)/2)
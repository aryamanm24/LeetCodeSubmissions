class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        stack = []
        primary = n

        while(n>0):
            stack.append(n%10)
            n = n//10
        
        second = 0
        length = len(stack)
        for i in range(length):
            second = (second*10) + stack[i]
        
        return abs(primary-second)
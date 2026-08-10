class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # if power is less than 0
        if(n < 0):
            x = 1/x # set x = 1/x; 2^-2 => (1/2)^2
            n = -n # in the above ex see how we transformed the power to be positive
        
        result = 1

        while(n>0):

            if(n%2 == 1):
                # do the 'itself' multiplication once
                result = result*x
            
            x = x*x
            n = n//2
        
        return result
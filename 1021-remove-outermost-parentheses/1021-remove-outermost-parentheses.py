class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        decompositions = []
        length = len(s)

        stack = []

        # since it's given that the str IS a valid paranthesis (given):
        # so, s[0] must be '(' and s[-1] must be ')' and also that s is not empty

        stack.append(s[0])

        ptr = 1
        open_count, closed_count = 1, 0

        while(open_count > closed_count or ptr < length):
            
            # restart counter if both are equal => indication that one decomposition has been done
            if(open_count == closed_count):
                decompositions.append("".join(stack))
                stack = []
                open_count, closed_count = 0, 0

            if(s[ptr] == '('):
                stack.append(s[ptr])
                open_count += 1
            
            elif(s[ptr] == ')'):
                stack.append(s[ptr])
                closed_count += 1
            
            ptr += 1

        # some decomposition was found but was not stored in the decompositions array as it came out of the loop
        if(len(stack) != 0):
            decompositions.append("".join(stack))

        string = ""

        for decomp in decompositions:
            # Assuming that every decomp at this point is a valid paranthesis in itself
            # removing is not possible => so, go for slicing instead
            string += decomp[1:-1]

        return string
        


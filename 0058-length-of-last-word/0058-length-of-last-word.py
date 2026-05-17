class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        i = len(s)-1

        while(i >= 0 and s[i] == " "):
            i-=1
        
        if(i < 0):
            return 0

        # Now we're at a decent word
        while(i>=0 and s[i] != " "):
            length += 1
            i-=1
        
        return length
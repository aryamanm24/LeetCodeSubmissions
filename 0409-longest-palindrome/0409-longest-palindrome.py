class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if(s == ""):
            return 0
        if(len(s) == 1):
            return 1
        
        # Building the palindrome from the outside and going inside

        frequency_map = {}

        for char in s:
            if(char not in frequency_map):
                frequency_map[char] = 0
            frequency_map[char] += 1

        length = 0
        
        for key in frequency_map:

            while(frequency_map[key] > 1):
                length += 2
                frequency_map[key] -= 2
        
        # Now find some char whose freq. = 1 and you can make an odd length palindrome
        # with the odd char in the dead center

        for key in frequency_map:
            if(frequency_map[key] == 1):
                length += 1
                frequency_map[key] -= 1
                break
        
        return length
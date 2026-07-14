class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if the two strings have different length, then they're not anagrams
        if(len(s) != len(t)):
            return False
        
        frequency_map_1 = {}
        frequency_map_2 = {}

        for char1, char2 in zip(s, t):
            if(char1 not in frequency_map_1):
                frequency_map_1[char1] = 0
            frequency_map_1[char1] += 1

            if(char2 not in frequency_map_2):
                frequency_map_2[char2] = 0
            frequency_map_2[char2] += 1
        
        for key in frequency_map_1:
            if(key not in frequency_map_2):
                return False
            else:
                if(frequency_map_1[key] != frequency_map_2[key]):
                    return False
        
        return True

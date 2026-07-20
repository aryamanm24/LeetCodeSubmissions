from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if the length of both words are not the same -> not anagrams
        if(len(s) != len(t)):
            return False

        s_char_frequency = defaultdict(int)
        t_char_frequency = defaultdict(int)

        for char1, char2 in zip(s, t):
            s_char_frequency[char1] += 1
            t_char_frequency[char2] += 1
        
        for key in s_char_frequency:
            if(key not in t_char_frequency):
                return False
            else:
                if(s_char_frequency[key] != t_char_frequency[key]):
                    return False
        
        return True
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for string in strs:

            char_vector = [0]*26 # O(1) -> since fixed size
            for char in string:
                char_vector[ord(char) - ord('a')] += 1
            
            anagrams[tuple(char_vector)].append(string)

        result = []

        for key in anagrams:
            result.append(anagrams[key])
        
        return result
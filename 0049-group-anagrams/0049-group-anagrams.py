from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for string in strs:

            count_arr = [0]*26

            for char in string:
                count_arr[ord(char) - ord('a')] += 1
            
            groups[tuple(count_arr)].append(string)
        
        final_result = []

        for key in groups:
            final_result.append(groups[key])

        return final_result
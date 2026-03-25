class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for string in strs:
            if(tuple(sorted(string)) not in hash_map):
                hash_map[tuple(sorted(string))] = [string]
            else:
                hash_map[tuple(sorted(string))].append(string)
        
        result = []

        for key in hash_map.keys():
            result.append(hash_map[key])
        
        return result
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for string in strs:

            key = tuple(sorted(string))

            if(key not in hash_map.keys()):
                hash_map[key] = [string]
            
            else:
                hash_map[key].append(string)
        
        result = []

        for key in hash_map.keys():
            result.append(hash_map[key])
        
        return result
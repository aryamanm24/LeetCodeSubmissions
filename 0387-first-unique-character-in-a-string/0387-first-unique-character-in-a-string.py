class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash_map = {}

        for i, char in enumerate(s):
            if(char in hash_map):
                hash_map[char] = -1
            else:
                hash_map[char] = i
        
        for key in hash_map.keys():
            if(hash_map[key] != -1):
                return hash_map[key]
        
        return -1
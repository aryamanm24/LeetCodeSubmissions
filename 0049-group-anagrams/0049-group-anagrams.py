class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tuple_map = {}

        for string in strs:

            key = tuple(sorted(string))

            if(key not in tuple_map):
                tuple_map[key] = []
            tuple_map[key].append(string)

        final_result = []

        for key in tuple_map:
            final_result.append(tuple_map[key])
        
        return final_result
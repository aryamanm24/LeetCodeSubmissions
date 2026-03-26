class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        insertions = 0
        open_count = 0

        for char in s:
            if(char == '('):
                open_count += 1
            else:
                if(open_count > 0):
                    open_count -= 1
                else:
                    insertions += 1
        
        return insertions + open_count
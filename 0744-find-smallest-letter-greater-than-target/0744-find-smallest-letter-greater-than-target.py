class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        target_num = ord(target)

        for char in letters:
            if(ord(char) > target_num):
                return char
        
        return letters[0]
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        # Two pointers -> one which goes to the front and one which goes backwards
        # The pointer that goes forward should keep on going forward --(1)
        # The pointer that goes backward should keep going backward --(2)
        # (1) and (2) anything other than that doesn't make sense

        length = len(words)
        word_double = [""]*(2*length)

        for d in range(0, length):
            if(words[(startIndex + d) % length] == target):
                return d
            if(words[(startIndex - d) % length] == target):
                return d
            
        return -1
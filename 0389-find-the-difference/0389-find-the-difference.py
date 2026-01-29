class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # So always, t.length = s.length + 1
        # And s and t could have the common elements (which are in s) in any order
        # But they will have the same ordered string

        # And then we could use two pointers to figure out the characters which
        # has been added

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        first, second = 0, 0
        length1 = len(s_sorted)
        length2 = len(t_sorted)

        while(first < length1):

            if(s_sorted[first] != t_sorted[second]):
                return t_sorted[second]
            
            first += 1
            second += 1
        
        # The added character is to the last of t_sorted
        return t_sorted[second]
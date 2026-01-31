class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        revised_string = ""

        for char in s:

            if(48 <= ord(char) <= 57 or 97 <= ord(char) <= 122):
                revised_string += char
            elif(65 <= ord(char) <= 90):
                revised_string += char.lower()
        
        left = 0
        right = len(revised_string)-1

        while(left <= right):
            if(revised_string[left] != revised_string[right]):
                return False
            right -= 1
            left += 1

        return True
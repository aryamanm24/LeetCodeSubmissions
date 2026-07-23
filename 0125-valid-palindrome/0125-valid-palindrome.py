class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word_list = []

        for char in s:
            if(char.isalnum()):
                word_list.append(char.lower())
        
        left = 0
        right = len(word_list) - 1

        while(left < right):
            if(word_list[left] != word_list[right]):
                return False
            
            left += 1
            right -= 1
        
        return True
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        max_length = 1
        hash_set = set()
        char = s[0]
        hash_set.add(char)

        left = 0
        right = 1

        while(right < len(s)):
            if(s[right] not in hash_set): # increase window
                hash_set.add(s[right])
                right += 1
                max_length = max(max_length, len(hash_set))
            else: # shrink window
                hash_set.remove(s[left])
                left += 1

        return max_length
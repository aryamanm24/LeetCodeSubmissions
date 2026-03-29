class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        # Since both strings are only 4 chaacters long and
        # the operation that we're allowed to do restricts
        # us to swapping i and j with a difference of 2

        # (i, j) = (0, 2) and (1, 3) -> Only possible pairs

        # only 4 words possible
        def swap_characters(s:string, first: int, second: int):

            word_list = list(s)
            word_list[first], word_list[second] = word_list[second], word_list[first]
            return ''.join(word_list)
        
        word_2 = swap_characters(s1, 0, 2)
        word_3 = swap_characters(s1, 1, 3)
        word_4 = swap_characters(word_2, 1, 3)

        acceptable_words = [s1, word_2, word_3, word_4]

        if(s2 in acceptable_words):
            return True
        return False
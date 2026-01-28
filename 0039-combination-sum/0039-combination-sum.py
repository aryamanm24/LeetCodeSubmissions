class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        length = len(candidates)

        def backtrack(current_list: List[int], current_index: int, remaining_target: int):
            
            # case where you considered an element which was greater than target and thus isn't
            # considered as a valid combo
            if(remaining_target < 0):
                return []
            # trivial base case and also the case where the target = 0, condition is satisfied

            if(remaining_target == 0):
                if(current_list != []):
                    result.append(current_list.copy())
            
            # to ensure that we never consider elements before index position current_index
            # to avoid duplicates from braches of recursion
            for index in range(current_index, length):

                current_list.append(candidates[index])
                backtrack(current_list, index, remaining_target - candidates[index])

                # whatever appending had to be done with that sequence would have been done
                # so to start fresh, remove all contents of current_list
                current_list.pop()
            
        
        candidates.sort()
        backtrack([], 0, target)

        return result
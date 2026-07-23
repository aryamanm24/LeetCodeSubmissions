class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_ptr = 0
        right_ptr = len(numbers)-1

        while(left_ptr < right_ptr):

            value = numbers[left_ptr] + numbers[right_ptr]
            if(value < target):
                left_ptr += 1
            elif(value > target):
                right_ptr -= 1
            else:
                return [left_ptr + 1, right_ptr + 1]
        
        return [-1, -1]
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()

        length = len(arr)

        result = []
        min_val = float('inf')

        for i in range(0, length-1):

            if(arr[i+1] - arr[i] < min_val):
                result = []
                min_val = arr[i+1] - arr[i]
                result.append([arr[i], arr[i+1]])
            
            elif(arr[i+1] - arr[i] == min_val):
                result.append([arr[i], arr[i+1]])
        
        return result
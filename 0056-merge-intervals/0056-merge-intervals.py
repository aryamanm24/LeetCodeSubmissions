class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        # [[1, 4], [1, 5], [4, 5]]

        result = [intervals[0]] # [1, 4]

        for start, end in intervals[1:]:

            # for i = 1, start = 1, end = 5 (from [1, 5])
            last_end = result[-1][1] # get the last end from the last element of result = 4
            if start <= last_end:
                result[-1][1] = max(last_end, end) # try to grab the max between the ends
            else:
                result.append([start, end]) # this works as we sorted the inner lists with the first element
        
        return result





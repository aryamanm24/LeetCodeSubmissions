class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])

        # So the first element has the shortest start
        # value at intervals[0][0]
        result = [intervals[0]]

        for start, end in intervals[1:]:

            if(start <= result[-1][1] <= end):
                result[-1][1] = end
            elif(start <= end <= result[-1][1]):
                continue
            else:
                interval = [start, end]
                result.append(interval)
        
        return result
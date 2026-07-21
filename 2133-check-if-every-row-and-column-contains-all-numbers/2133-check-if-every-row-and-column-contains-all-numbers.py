class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)

        def isPermutation(values):

            seen = set(values)

            for i in range(1, n+1):
                if(i not in seen):
                    return False
            
            return True
            
        for row in matrix:
            if(not isPermutation(row)):
                return False
        
        # building the column values
        for col in range(n):
            col_values = []
            for row in range(n):
                col_values.append(matrix[row][col])
            if(not isPermutation(col_values)):
                return False
        
        return True
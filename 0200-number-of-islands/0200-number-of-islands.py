class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if(not grid):
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def sink(row, col):
            if(row<0 or row>=rows or col<0 or col>=cols or grid[row][col] == '0'):
                return
            
            # otherwise, the grid value which was '1' has been considered, so turn it to '0'
            grid[row][col] = '0'
            sink(row-1, col)
            sink(row+1, col)
            sink(row, col-1)
            sink(row, col+1)

        count = 0

        for row in range(rows):
            for col in range(cols):
                if(grid[row][col] == '1'):
                    count += 1
                    sink(row, col)
        
        return count
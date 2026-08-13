class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # boxes = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        for row in range(9):
            for col in range(9):

                value = board[row][col]
                if(value != '.'):

                    box_row = row//3
                    box_col = col//3

                    box_index = (box_row * 3) + box_col

                    if(value in rows[row]):
                        return False
                    
                    if(value in cols[col]):
                        return False
                    
                    if(value in boxes[box_index]):
                        return False
                    
                    rows[row].add(value)
                    cols[col].add(value)
                    boxes[box_index].add(value)
        
        return True
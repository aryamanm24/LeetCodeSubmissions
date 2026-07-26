class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows_sets = [set() for _ in range(9)]
        cols_sets = [set() for _ in range(9)]
        boxes_sets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                value = board[row][col]

                # computing box index:
                box_row = row//3
                box_col = col//3
                box_index = (box_row*3) + box_col
                # if cell is not empty, then check
                if(value != "."):
                    if(value in rows_sets[row]):
                        return False
                    if(value in cols_sets[col]):
                        return False
                    if(value in boxes_sets[box_index]):
                        return False
                    
                    rows_sets[row].add(value)
                    cols_sets[col].add(value)
                    boxes_sets[box_index].add(value)
        
        return True
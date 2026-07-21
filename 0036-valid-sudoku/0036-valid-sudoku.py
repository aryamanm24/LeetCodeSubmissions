class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # length of the board is fixed
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # rows = [(), (), (), (), (), (), (), (), ()]
        # cols = [(), (), (), (), (), (), (), (), ()]
        # boxes = [(), (), (), (), (), (), (), (), ()]

        # box logic -> box_row = row//3
        # box_col = col//3
        # box_index (in the list of sets) = (box_row)*3 + box_col

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if(value != "."):
                    box_row = row//3
                    box_col = col//3
                    box_index = (box_row*3) + box_col
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
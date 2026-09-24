class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] in seen:
                    print(f"rows {r} {c}")
                    return False
                elif board[r][c] != ".":
                    seen.add(board[r][c])
        
        # check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] in seen:
                    print(f"cols {r} {c}")
                    return False
                elif board[r][c] != ".":
                    seen.add(board[r][c])
        
        # check boxes
        for i in range(3):
            for j in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[i*3+r][j*3+c] in seen:
                            print(f"boxs {i*3+r} {j*3+c}")
                            return False
                        elif board[i*3+r][j*3+c] != ".":
                            seen.add(board[i*3+r][j*3+c])
        
        return True

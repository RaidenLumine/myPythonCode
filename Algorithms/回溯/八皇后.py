from typing import List
import math

class NQueens:
    def solve(self, n: int) -> List[List[int]]:
        def safe(board: List[int], row: int, col: int) -> bool:
            for i in range(row):
                if board[i] == col or math.fabs(board[i] - col) == math.fabs(i - row):
                    return False
            return True

        def backtrack(row: int, board: List[int], solutions: List[List[int]], n: int) -> None:
            if row == n:
                solutions.append(board[:])
                return
            for col in range(n):
                if safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board, solutions, n)
                    board[row] = -1

        solutions = []
        board = [-1] * n
        backtrack(0, board, solutions, n)
        return solutions


if __name__ == "__main__":
    nqueens = NQueens()
    n = int(input("请输入皇后数量："))
    numOfSolutions = nqueens.solve(n)
    print(f"{n} 皇后问题有 {len(numOfSolutions)} 种解法。")
# 编写一个程序，通过填充空格来解决数独问题。

# 数独的解法需 遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。

# 示例 1：
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

# 提示：
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解

from typing import List
class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board or len(board) != 9 or len(board[0]) != 9:
            return
        row=[[False] * 9 for _ in range(9)]
        col=[[False] * 9 for _ in range(9)]
        box=[[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                num=ord(board[i][j])-ord('1')
                k=(i//3)*3+j//3
                row[i][num]=col[j][num]=box[k][num]=True
                
        self.backtrack(board,0,row,col,box)

    def backtrack(self, board: List[List[str]], n: int, row: List[List[bool]], col: List[List[bool]], box: List[List[bool]]) -> bool:
            if n == 81:
                return True
            i,j=n//9,n%9
            if board[i][j]!='.':
                return self.backtrack(board,n+1,row,col,box)
            k=(i//3)*3+j//3
            for num in range(9):
                if not row[i][num] and not col[j][num] and not box[k][num]:
                    board[i][j]=str(num+1)
                    row[i][num]=col[j][num]=box[k][num]=True
                    if self.backtrack(board,n+1,row,col,box):
                        return True
                    row[i][num]=col[j][num]=box[k][num]=False
            board[i][j]='.'
            return False
        
        

if __name__ == "__main__":
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    s = Solution()
    s.solveSudoku(board)
    for row in board:
        print(row)
res = []

# 记录原本的
# question = ["000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000"]

# board = ["000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000",
#          "000000000"]

question = [[1, 2, 3], [0, 0, 0], [0, 0, 0]]
# board = [[1, 2, 3], [0, 0, 0], [0, 0, 0]]
# board = [
#  [6, 9, 5, 1, 2, 3, 7, 4, 8],
#  [7, 4, 1, 8, 6, 9, 2, 5, 3],
#  [2, 3, 8, 4, 5, 7, 1, 6, 9],
#  [8, 1, 6, 7, 4, 5, 3, 9, 2],
#  [5, 2, 4, 3, 9, 8, 6, 7, 1],
#  [3, 7, 9, 6, 1, 2, 4, 8, 5],
#  [4, 8, 3, 9, 7, 1, 5, 0, 0],
#  [1, 6, 2, 5, 8, 4, 9, 0, 0],
#  [9, 5, 7, 2, 3, 6, 8, 0, 0]
# ]
board = [
    [0,0,1,0,0,3,0,0,0],
    [0,0,0,8,5,0,0,0,0],
    [0,4,0,0,2,6,8,0,0],
    [0,7,9,0,0,5,0,0,2],
    [0,0,2,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,2,7],
    [6,0,0,0,4,0,0,0,0],
    [0,0,0,1,9,0,6,8,0]
]

n = m = 9

# 路径board中的row已经完成
# 选择列表，一行中还没有的数字
# row超过board
def backtrack(board, row, col):
    # print(board, row, col)
    if col == 9:  # 列
        # 穷举到最后一列的话就换到下一行重新开始
        return backtrack(board, row + 1, 0)  # 这个return很重要
    if row == 9:  # 成功
        # 找到一个可行解，触发 base case
        return True
    if board[row][col] != 0:  # 预设数字
        return backtrack(board, row, col + 1)  # todo 在这里没有返回所有一直错 一定要有返回值才能结束

    # else:
    #     for k in range(1, 10):
    #         # 不合适则跳过
    #         if not check(board, row, col, k):
    #             continue
    #         board[row][col] = k
    #         if backtrack(board, row, col + 1):
    #             return True
    #         board[row][col] = 0
    # return False


    # 每个位置进行穷举
    for i in range(row, n):
        for j in range(col, m):
            if board[i][j] != 0:  # 预设数字
                backtrack(board, i, j + 1)
                return
            for k in range(1, n+1):
                # 不合适则跳过
                if not check(board, i, j, k):
                    continue
                board[i][j] = k
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = 0
            return False
    return False


def check(board, row, col, num):
    for i in range(n):
        # if board[row][i] == num and i != col:  # 放进去之前检查，所以不用i!=col
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
        # 判断3*3方框中是否存在重复
        # if board[(row//3)*3+i//3][(col//3)*3+i % 3] == num:
        #     return False
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if board[i][j] == num:
                return False
    return True


b = backtrack(board, 0, 0)
print(board)
print(b)

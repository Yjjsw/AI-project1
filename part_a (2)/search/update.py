import math

board_size = 7  # board size
pos_limit = board_size - 1
move_set = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]  # all possible moving directions
# 定义向上为+1，-1 向下就是-1，+1，向左上0，-1，向右下0，+1，左下-1,0，右上+1,0

# return the new coordinate when moving token at (x,y) towards direction 1 step
# 测试过move，没问题
def move(coordinate, direct) -> tuple:
    new_x = (coordinate[0] + direct[0]) % board_size
    new_y = (coordinate[1] + direct[1]) % board_size
    return (new_x, new_y)


# 给定棋子的coordinate(2,1)和direction（0，1）去更新board，其中包含了spread
# 测试过update，没问题
def update_board(board, coord, direct=None) -> dict[tuple, tuple]:
    x = coord[0]
    y = coord[1]
    color = board[coord][0]
    power = board[coord][1]
    del board[coord] # 删除当前棋子，可能需要等所有的action都得到后再pop掉
    while power > 0:  # 用一个loop来让棋子一格格移动，power有多少就移动多少个的1
        next = move((x, y), direct)
        if next in board:  # 当前格子已经有棋子了（吃子）
            board[next] = (color, board[next][1] + 1)  # 当前格子的power+1(因为被占领吃掉了)
        else:
            board[next] = (color, 1)
        power -= 1
        x += direct[0]  # 如果power大于1，那么还需要用x继续往相同的方向移动棋子
        y += direct[1]
    return board

import math

board_size = 7  # board size
pos_limit = board_size - 1
move_set = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]  # all possible moving directions


# return the new coordinate when moving token at (x,y) towards direction 1 step
def move(x, y, direct) -> tuple:
    new_x = (x + direct[0]) % (board_size)
    new_y = (y + direct[1]) % (board_size)
    return (new_x, new_y)


# update board after splitting the token at coord towards the direct
def update_board(board, coord, direct=None) -> dict[tuple, tuple]:
    x = coord[0]
    y = coord[1]

    color = board[coord][0]
    p = board[coord][1]
    del board[coord]
    while p > 0:
        next = move(x, y, direct)
        if next in board:
            board[next] = (color, board[next][1] + 1)
        else:
            board[next] = (color, 1)
        p -= 1
        x += direct[0]
        y += direct[1]
    return board


# return the closest red token and shortest path, take power of token into consideration
# used for generate approximate solution
def find_closest(board, coord) -> (tuple, list):
    best_token = None
    best_path = [0, 0, 0, 0, 0, 0]  # number of moves in each direction
    best_distance = pos_limit * 2
    # find distance and path with first 4 moving directions
    for token in board:
        if board[token][0] == 'r':
            path = [0, 0, 0, 0, 0, 0]
            # x distance
            x_warp = False
            if math.fabs(token[0] - coord[0]) > board_size / 2:  # warp is closer
                x_warp = True
            x_dist = math.fabs(token[0] - coord[0]) % board_size
            x_direct = (coord[0] - token[0]) / math.fabs(token[0] - coord[0])
            if x_warp:
                x_direct *= -1
            if x_direct == 1:
                path[0] = x_dist
            else:
                path[1] = x_dist
            # y distance
            y_warp = False
            if math.fabs(token[1] - coord[1]) > board_size / 2:  # warp is closer
                y_warp = True
            y_dist = math.fabs(token[1] - coord[1]) % board_size
            y_direct = (coord[1] - token[1]) / math.fabs(token[1] - coord[1])
            if y_warp:
                y_direct *= -1
            if y_direct == 1:
                path[2] = y_dist
            else:
                path[3] = y_dist
            # merge (1,0) and (0,-1) into (1,-1)

"""给定一个颜色和board，数这个board中这个颜色的数量，如果红色多就用红色消除蓝色（棋子越多需要消掉所有棋子需要的步骤就越多）
    当前检测的是蓝色的棋子数，因为单人模式只能操作红色棋子"""

def count_number(board, color='b') -> int:
    count = 0;
    for temp in board.values():  # 让temp变成颜色,如果和检测的color相同，那么count++（现在检测的是蓝色的棋子数）
        current_color = temp[0]
        if current_color == color:
            count += 1
    return count


"""用来看action list，就是棋子能往哪里移动，如果有n个棋子总长就是6n"""

def get_action_list(board: dict[tuple, tuple], color) -> list:
    return


def calculate_heuristic(board: dict[tuple, tuple]) -> int:
    return

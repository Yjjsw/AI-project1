"""给定一个颜色和board，数这个board中这个颜色的数量，如果红色多就用红色消除蓝色（棋子越多需要消掉所有棋子需要的步骤就越多），
    这里是最初代的heuristic算法,之后需要更新
    当前需要检测的是蓝色的棋子数，因为单人模式只能操作红色棋子"""
"""测试过，没问题"""


def count_number(board: dict[tuple, tuple], color) -> int:
    count = 0
    for temp in board.values():  # 让temp变成颜色,如果和检测的color相同，那么count++（现在检测的是蓝色的棋子数）
        current_color = temp[0]  # 这里的0是因为value有两个值，一个power一个color，所以只需要提取第一个值就是color
        if current_color == color:
            count += 1
    return count


"""将修改过的heuristic方法写在下面的function中，这里第一种count number方法没有考虑到棋子power的问题，学长默认了
    一个棋子只能吃一个棋，就会导致count number方法不是admissible，改进后可以看到会考虑棋子的power值，但是运行时间过长"""


def calculate_heuristic(board: dict[tuple, tuple]) -> int:
    max_power = 0
    for temp in board.values():
        if temp[0] == 'r':  # 检测是否是红色棋子
            if temp[1] > max_power:  # 检测power是否是最大值
                max_power = temp[1]
    final = count_number(board, 'b') - max_power
    return final


"""计算g值的函数，这个g的计算⽅式是当前节点到起始节点的距离加上下⼀个节点的距离，所以其实不需要运算，只要每次child节点+1即可"""


def calculate_g(board) -> int:
    return

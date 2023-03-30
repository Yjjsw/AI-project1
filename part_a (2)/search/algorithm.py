from heuristic import count_number

"""A node class for A* Pathfinding"""


class Node():

    def __init__(self, parent=None, position=None, move=None):
        self.parent = parent
        self.position = position
        self.move = move  # 这里的move就是action(就是移动)
        self.g = 0
        self.h = 0
        self.f = 0


"""得到actionlist，这里需要看慧敏action是怎么写的"""


"""用来找到所有的开始节点，在project1中就是记录所有的red的棋子位置"""


def all_start(board) -> list[Node]:
    cur_position = []
    cur_node = Node(None, None, None)  # 新建一个node
    color = 'r'
    for position, temp in board.items():
        if temp.value[0] == color:  # 只有当color是红色才会append进list中
            cur_node.position = position
            cur_node.move = get_actionlist(board)  # 得到action list，这里要看慧敏怎么得到一个position的所有action
            cur_position.append(cur_node)
    return cur_position


""" 需要输入一个board,start-node和end-node就可以得到所有相应的操作，这里的list就是最后的答案（project1需要的最后输出）
    Reference：
    https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
"""

def a_star(board) -> list[tuple]:
    start_node_list = all_start(board)
    start_node_list.g = 0
    start_node_list.h = 0
    start_node_list.f = 0
    leaf_list = []  ##对应那些没有child的节点
    already_list = []  ##对应已经读取过的节点
    for cur_node in start_node_list:  # 将所有的start node都放入list中
        leaf_list.append(cur_node)

    while len(leaf_list) > 0:  # 只要还有起始点，说明还有可能有更优解
        cur_node = leaf_list[0]
        node_index = 0
        for index, item in enumerate(leaf_list):  ##enumerate会和正常loop一样循环，但是会多一个index来指示这是第几个循环
            if item.f < cur_node.f:  ##如果f比现有的小，说明这个节点的方案优于当前方案，所以替换掉当前节点
                node_index = index
                cur_node = item

        leaf_list.pop(cur_node)
        already_list.append(cur_node)

        """goal test,看是否找到了正确解，这里的正确解就是一方的棋子数为0"""
        goal_test = count_number(board, 'b')
        if goal_test == 0:
            final_path = []
            current = cur_node
            while current is not None:
                final_path.append(current.position)
                current = cur_node.parent ##这样current就不会变成none除非当前节点的parent为空
            return final_path[::-1]##倒着找回去

        ##47.36 如何生成child（parent）
        child = []
        for action_list in []


    return

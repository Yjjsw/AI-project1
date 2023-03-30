
"""A node class for A* Pathfinding"""


class Node():

    def __init__(self, parent=None, position=None, move=None):
        self.parent = parent
        self.position = position
        self.move = move # 这里的move就是action(就是移动)
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
            cur_node.move = get_actionlist(board) #得到action list，这里要看慧敏怎么得到一个position的所有action
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
    leaf_list = []##对应那些没有child的节点
    already_list = []##对应已经读取过的节点
    for cur_node in start_node_list:#将所有的start node都放入list中
        leaf_list.append(cur_node)

    while len(leaf_list) > 0:#只要还有起始点，说明还有可能有更优解


    return

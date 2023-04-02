from search.heuristic import count_number
from search.update import move_set, update_board, move

"""A node class for A* Pathfinding"""


class Node():

    def __init__(self, parent=None, position=None, move=None):
        self.parent = parent
        self.position = position
        self.move = move  # 这里的move就是action(就是移动)
        self.g = 0
        self.h = 0
        self.f = 0


""" 得到spread list，简单来说就是得到一个向量坐标tuple，然后得到这个坐标相应的6个方向的action并放入list中
    output的例子[((6,5),(0,1)),((6,5),(0,-1))],注意这里只是得到棋子的position以及output棋子可以move的方向"""
"""测试过，没问题"""


def generate_spread_list(position) -> list:
    spread_list = []
    six_direction = move_set  # 6个方向
    count = 0
    for i in range(6):  # 6个方向
        spread_list.append((position, six_direction[count]))
        count += 1
    return spread_list


"""用来找到所有的开始节点，在project1中就是记录所有的red的棋子位置"""


# test过all start,没问题

def all_start(board) -> list[Node]:
    node_list = []
    cur_node = Node(None, None, None)  # 新建一个node
    color = 'r'
    for position, temp in board.items():
        if temp[0] == color:  # 只有当color是红色才会append进list中
            cur_node.position = position
            cur_node.move = generate_spread_list(position)  # 得到action list，这里要看慧敏怎么得到一个position的所有action
            node_list.append(cur_node)
    return node_list


""" 需要输入一个board就可以得到所有相应的操作，这里的list就是最后的答案（project1需要的最后输出）
    Reference：
    https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
"""


def a_star(board) -> list[tuple]:  # path最后形式(5, 6, -1, 1)，这里得出来的path
    start_node_list = all_start(board)

    unused_list = []  # 对应那些没有child的节点
    used_list = []  # 对应已经读取过的节点，这两个list的作用是遍历几乎所有的棋盘来看什么时候达到goal test，达到后再通过当前棋子的parent来找path
    for cur_node in start_node_list:  # 将所有的start node初始化并都放入list中，因为project1中start node只有红色的棋子，所以这里start node不考虑蓝色棋子
        cur_node.g = 0
        cur_node.h = count_number(board, 'b')
        cur_node.f = 0
        unused_list.append(cur_node)

    while len(unused_list) > 0:  # 只要还有起始点，说明还有可能有更优解
        cur_node = unused_list[0]
        node_index = 0  # index未使用过
        for index, item in enumerate(unused_list):  # enumerate会和正常loop一样循环，但是会多一个index来指示这是第几个循环
            if item.f < cur_node.f:  ##如果f比现有的小，说明这个节点的方案优于当前方案，所以替换掉当前节点
                node_index = index
                cur_node = item

        unused_list.remove(cur_node)
        used_list.append(cur_node)

        # goal test,看是否找到了正确解，这里的正确解就是blue方的棋子数为0
        goal_test = count_number(new_board, 'b')
        if goal_test == 0:
            final_path = []
            current = cur_node
            while current is not None:
                final_path.append(current.position)  # 根据node中的parent找path，而不是根据unused_list或used_list找
                current = cur_node.parent  ##这样current就不会变成none除非当前节点的parent为空
            return final_path[::-1]  ##倒着找回去

        # 找到了当前最优节点之后再开始看它的child,先新建child list，将位置，parent和move都定义好
        child_node_list = []

        for action_list in cur_node.move:  # 这里的action list就是一个tuple((6,5),(0,1))         因为这里的move只有6个，所以child只有6个
            new_board = update_board(board, action_list[0], action_list[1]) #更新棋盘

            new_child_node = Node(cur_node, move(cur_node.position, cur_node.move[1]), None)
            new_child_node.move = generate_spread_list(new_child_node.position)
            # 这里初始化child，child node的parent是当前的node，它的position根据读取的哪一个move来计算，move通过function来得到，同时更新g，h和f值
            child_node_list.append(new_child_node)



        print(len(child_node_list))
        break
        """test"""
        for child in child_node_list:
            for check_used in used_list:  # 如果在used_list中，就不需要再管，因为这个node被访问过了就已经在最终答案中了
                if child == check_used:
                    continue

            for check in unused_list:  # 如果在unused_list中，说明这个child节点其实还在备选名单unused list中，已经赋值过初始化过了
                if child == check:
                    continue
            # 最后给child的g，h，f赋值
            child.g = cur_node.g + 1
            child.h = count_number(new_board, 'b')
            child.f = child.g + child.h

            unused_list.append(child)
    return

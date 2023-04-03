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


def generate_spread_list(position) -> list[tuple]:
    spread_list = []
    six_direction = move_set  # 6个方向
    count = 0
    for i in range(6):  # 6个方向
        spread_list.append((position, six_direction[count]))
        count += 1
    return spread_list


"""需要根据当前棋子的power和各个方向（上面生成的spread_list）得到所有可能的child的position和direction，
    比如如果power为1，那么就只有6个child，power为2，就有12个child"""
"""test过，无问题,output的形式为[((6, 6),(1,-1)), ...]，其中6，6是这个方向的child，1，-1是方向"""


def generate_child_list(board, position, spread_list) -> list[tuple]:
    child_list = []
    for value in spread_list:  # 得到6个方向，再对每个方向进行spread操作
        x = position[0]
        y = position[1]
        power = board[position][1]  # 当前棋子的power
        direct = value[1]
        while power > 0:
            cur_child = move((x, y), direct)  # direct得到原点的移动方向
            power -= 1
            x += direct[0]  # 如果power大于1，那么还需要用x继续往相同的方向移动棋子
            y += direct[1]
            child_list.append((cur_child, direct))
    return child_list


"""用来找到所有的开始节点，在project1中就是记录所有的red的棋子位置"""
"""test过all start,没问题"""


def all_start(board) -> list[Node]:
    node_list = []
    cur_node = Node(None, None, None)  # 新建一个node
    color = 'r'
    for position, temp in board.items():
        if temp[0] == color:  # 只有当color是红色才会append进list中
            cur_node.position = position
            cur_node.move = generate_spread_list(position)
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
    for new_node in start_node_list:  # 将所有的start node初始化并都放入list中，因为project1中start node只有红色的棋子，所以这里start node不考虑蓝色棋子
        new_node.g = 0
        new_node.h = count_number(board, 'b')
        new_node.f = 0
        unused_list.append(new_node)
    parent_node = unused_list[0]  # 初始化之前的节点
    "用计数器来test，使得loop跑规定次数的循环"
    test_count = 0

    while len(unused_list) > 0:  # 只要还有起始点，说明还有可能有更优解
        cur_node = unused_list[0]
        node_index = 0  # index未使用过
        for index, item in enumerate(unused_list):  # enumerate会和正常loop一样循环，但是会多一个index来指示这是第几个循环
            if item.f < cur_node.f:  ##如果f比现有的小，说明这个节点的方案优于当前方案，所以替换掉当前节点
                node_index = index
                cur_node = item

        unused_list.remove(cur_node)
        used_list.append(cur_node)

        # 让cur_node和之前的node比较，如果两个坐标一样，说明没有move（只有第一次是这种情况，后面的node都会被移出unused list中），如果两个坐标不一样，互相减一下就能得到方向
        # 比如新的坐标为6，6，之前的坐标为5,6，只需要用6，6 - 5,6就能得到1,0，也就是5,6 spread的方向
        if cur_node.position != parent_node.position:  # 两者的node的位置不同
            x = cur_node.position[0] - parent_node.position[0]
            y = cur_node.position[1] - parent_node.position[1]
            direct = (x, y)  # 得到方向
            update_board(board, parent_node.position, direct)
            del board[parent_node.position]  # 删掉老节点
            parent_node = cur_node  # 更新parent_node
        else:  # 第一次,不需要做任何事,下面一行的操作是用来凑数的,因为不能用continue
            parent_node = cur_node


        # goal test,看是否找到了正确解，这里的正确解就是blue方的棋子数为0
        goal_test = count_number(board, 'b')
        if goal_test == 0:
            final_path = []
            current = cur_node
            while current is not None:
                final_path.append(current.position)  # 根据node中的parent找path，而不是根据unused_list或used_list找
                current = cur_node.parent  ##这样current就不会变成none除非当前节点的parent为空
            return final_path[::-1]  ##倒着找回去

        # 找到了当前最优节点之后再开始看它的child,先新建child list，将位置，parent和move都定义好,并初始化count，为后面loop使用
        child_node_list = []
        child_position_list = generate_child_list(board, cur_node.position, cur_node.move)
        count = 0
        for value in cur_node.move:  # 得到6个方向
            direct = value[1]
            board = update_board(board, cur_node.position, direct)  # 更新棋盘,这样就是只往6个方向spread每个方向spread一次
            power = board[cur_node.position][1]  # 得到当前棋子的power
            for loop_time in range(power):  # 有多大power就循环几次，这样可以循环6个方向*power次，从而得到所有的child

                child_position = child_position_list[count][0]  # 这里的child_position_list就是一个装满了对应所有child的位置

                for check in used_list:
                    check_position = check.position
                    if check_position == child_position:  # 如果在used_list中，说明不是初始化
                        already_in = True
                        break
                    else:
                        already_in = False
                if not already_in:
                    count += 1  # 使得根据power的大小而改变
                    new_child_node = Node(cur_node, child_position, None)
                    new_child_node.move = generate_spread_list(new_child_node.position)
                    # 这里初始化child，child node的parent是当前的node，它的position根据读取的哪一个move来计算，move通过function来得到

                    # 最后给child的g，h，f赋值，这里就需要赋值是因为只有在这里棋盘才更新了
                    new_child_node.g = cur_node.g + 1
                    new_child_node.h = count_number(board, 'b')
                    new_child_node.f = new_child_node.g + new_child_node.h
                    child_node_list.append(new_child_node)

                    del board[child_position]  # 删除child节点，因为初始化结束了

        print(parent_node.position)
        print(cur_node.position)
        test_count += 1
        if (test_count == 2):
            break
        """test"""


        for child in child_node_list:
            for check_used in used_list:  # 如果在used_list中，就不需要再管，因为这个node被访问过了就已经在最终答案中了，
                if child == check_used:
                    continue  # continue的作用是跳过当前child，不把它append进unused list中

            for check in unused_list:  # 如果在unused_list中，说明这个child节点其实还在备选名单unused list中，已经赋值过初始化过了
                if child == check:
                    continue

            unused_list.append(child)

    return

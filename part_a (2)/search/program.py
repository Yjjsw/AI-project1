# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from search.algorithm import a_star, generate_child_list, generate_spread_list  # 记住加文件夹名search.
from search.update import update_board
import time

from .utils import render_board


def search(input: dict[tuple, tuple]) -> list[tuple]:
    print(render_board(input, ansi=True))

    """test 用, test count number
    start = time.time()
    spread_list = update_board(input,(5,6),(0,1))
    print(spread_list)
    end = time.time()
    print('Running time: %s Seconds' % (end - start))"""
    spread_list = a_star(input)
    print(render_board(input, ansi=True))

    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]

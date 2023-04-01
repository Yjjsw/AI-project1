# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from search.algorithm import generate_spread_list  # 记住加文件夹名search.
from search.heuristic import count_number

from .utils import render_board


def search(input: dict[tuple, tuple]) -> list[tuple]:
    print(render_board(input, ansi=True))

    """test 用, test count number"""
    spread_list = count_number(input, 'r')
    print(spread_list)

    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]

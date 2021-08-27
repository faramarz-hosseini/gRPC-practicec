from typing import Union, Tuple


def do_operations(num: int) -> Tuple[int, int, int, float]:
    add = num + num
    sub = str(num - num)
    multi = num * num
    division = int(num / num)

    return add, sub, multi, division



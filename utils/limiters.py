from typing import List
from middlewares.settings import DEFAULT_LIMIT


def transform_keyboard(transform_list: List) -> List:
    current_list = []
    count = 0

    for item in range(len(transform_list)):
        if count < DEFAULT_LIMIT:
            current_list.append(item)
            current_list[item] = 1
            count += 1
    return current_list


def pages_limiter(number: int, count: int = 2):
    if number % 2 == 0:
        limit = int(number / count)
        return limit
    else:
        limit = int(number / count) + 1
        return limit

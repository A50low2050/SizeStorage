from typing import List
from middlewares.settings import DEFAULT_LIMIT


def limiter_models(models: List) -> List:
    current_model = []
    count = 0

    for item in range(len(models)):
        if count < DEFAULT_LIMIT:
            current_model.append(item)
            current_model[item] = 1
            count += 1
    return current_model


def pages_limiter(number: int, count: int = 2):
    if number % 2 == 0:
        limit = int(number / count)
        return limit
    else:
        limit = int(number / count) + 1
        return limit

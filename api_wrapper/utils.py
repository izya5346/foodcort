import functools
from typing import List
@functools.lru_cache(maxsize=8192)
def find(value: str, ls, key: str = 'restaurant_id'):
    for i in ls:
        if value in i[key]:
            yield i
        
from typing import TypeVar, List

T = TypeVar('T')

def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]

print(reverse_list(items=[1, 2, 3, 4, 5]))
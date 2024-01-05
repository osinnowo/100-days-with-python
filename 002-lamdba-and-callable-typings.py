from typing import List, Callable

# custom function
def process(items: List[int], condition: Callable[[int], bool]) -> bool:
    for item in items:
        if condition(item):
            return True
    else:
        return False

# With filter() function
def greater_than_value_filtering(items: List[int], value: int) -> List[int]:
    filtered = list(filter(lambda x: x >= value, items))
    return filtered


# With map() function
def transform_values(items: List[int], by: int) -> List[int]:
    result = list(map(lambda item: item * by, items))
    return result


# Testing
item = process(items=[1, 2, 3, 4, 5, 6], condition=lambda x: x >= 25)
print(item)

lists: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
print(greater_than_value_filtering(items=lists, value=3))
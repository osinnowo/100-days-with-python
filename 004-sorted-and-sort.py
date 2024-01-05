from typing import List

def sorted_items(items: List[int]):
    return sorted(items)


def sort_items(items: List[int]) -> List[int]:
    items.sort()
    return items


lists = [9, 8, 6, 7, 1, 2, 3, 4, 5]

print(sorted_items(items=lists))
print(lists)

print(sort_items(items=lists))
print(lists)
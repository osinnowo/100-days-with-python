from typing import List


def reverse_an_array_custom(array: List[int]) -> List[int]:
    for i in range(len(array) // 2):
        last_index = len(array) - i - 1
        item = array[i]
        array[i] = array[last_index]
        array[last_index] = item
    else:
        return array


def reverse_an_array_with_slicing(array: list[int]) -> list[int]:
    return array[::-1]


print(reverse_an_array_custom(array=[0, 1, 2, 3, 4, 5, 6]))
print(reverse_an_array_with_slicing(array=[0, 1, 2, 3, 4, 5, 6]))


#from util import time_it

#@time_it
def linear_search(numbers_list, number_to_find):
    """
    Perform a linear search on the list to find the index of the given number.

    Args:
    numbers_list (list): The list of numbers to search through.
    number_to_find (int): The number to find in the list.

    Returns:
    int: The index of the number if found, otherwise -1.
    """
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

#@time_it
def binary_search(numbers_list, number_to_find):
    """
    Perform an iterative binary search on the sorted list to find the index of the given number.

    Args:
    numbers_list (list): The sorted list of numbers to search through.
    number_to_find (int): The number to find in the list.

    Returns:
    int: The index of the number if found, otherwise -1.
    """
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    """
    Perform a recursive binary search on the sorted list to find the index of the given number.

    Args:
    numbers_list (list): The sorted list of numbers to search through.
    number_to_find (int): The number to find in the list.
    left_index (int): The starting index of the current search range.
    right_index (int): The ending index of the current search range.

    Returns:
    int: The index of the number if found, otherwise -1.
    """
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 2999

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    print(f"Number found at index {index} using binary search")

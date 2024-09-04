"""
This is the python file of mergeSort
"""

import rand


def merge_sort(arr):
    """
    This is the main function of mergeSort
    """

    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    This is the function to merge the two halves.
    """
    left_index = 0
    right_index = 0
    merge_arr = [0] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    merge_sub_array(left_index, right_index, right_arr, merge_arr)
    merge_sub_array(right_index, left_index, left_arr, merge_arr)

    return merge_arr

def merge_sub_array(start_index: int, sub_start_index: int, sub_arr: list[int], merge_arr: list[int]):
    for i in range(sub_start_index, len(sub_arr)):
        merge_arr[start_index + sub_start_index] = sub_arr[i]

target_arr = rand.random_array([None] * 20)
arr_out = merge_sort(target_arr)

print(arr_out)

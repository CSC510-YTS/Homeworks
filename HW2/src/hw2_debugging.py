"""
This is the python file of mergeSort
"""
from HW2.src import rand
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
        if (left_arr[left_index] < right_arr[right_index]):
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
        merge_sub_array(
            left_index,
            right_index,
            right_arr,
            left_arr,
            merge_arr)

    return merge_arr


def merge_sub_array(
        left_index: int,
        right_index: int,
        right_arr: list[int],
        left_arr: list[int],
        merge_arr: list[int]):
    """
    The helper method to merge sub array
    """
    sub_arr = right_arr if right_index < len(right_arr) else left_arr
    sub_start_index = right_index if right_index < len(
        right_arr) else left_index
    start_index = left_index if right_index < len(right_arr) else right_index

    for i in range(sub_start_index, len(sub_arr)):
        merge_arr[start_index + i] = sub_arr[i]


target_arr = rand.random_array([None] * 20)
arr_out = merge_sort(target_arr)

print(arr_out)

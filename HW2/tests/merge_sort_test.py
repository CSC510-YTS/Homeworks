import pytest
import copy
from HW2.src.hw2_debugging import merge_sort


def test_merge_sort_ascending_ordered_array():
    ascending_sorted_array = [x for x in range(1, 50)]
    ascending_sorted_array_deep_copy = copy.deepcopy(ascending_sorted_array)
    sorted_array = merge_sort(ascending_sorted_array_deep_copy)

    assert sorted_array == ascending_sorted_array_deep_copy


def test_merge_sort_random__unsorted_array():
    random_unsorted_array = [2, 1, 25, 89, -1, 6, 8, 4]
    sorted_array = merge_sort(random_unsorted_array)

    assert sorted_array == [-1, 1, 2, 4, 6, 8, 25, 89]


def test_merge_sort_descending_ordered_array():
    descending_sorted_array = [x for x in range(50, 0, -1)]
    sorted_array = merge_sort(descending_sorted_array)

    assert sorted_array == sorted(descending_sorted_array)
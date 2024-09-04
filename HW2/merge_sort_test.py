import pytest
import copy
from hw2_debugging import merge_sort

def test_merge_sort():
    ascending_sorted_array = [x for x in range(1, 50)]
    ascending_sorted_array_deep_copy = copy.deepcopy(ascending_sorted_array)
    merge_sort(ascending_sorted_array_deep_copy)

    assert ascending_sorted_array == ascending_sorted_array_deep_copy

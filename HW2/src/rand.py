"""
This file is to grenarte a random array
"""
import subprocess


def random_array(arr):
    """
    This function is to grenarte a random array
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr

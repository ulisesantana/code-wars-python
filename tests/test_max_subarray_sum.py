def max_sequence(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def test_max_subarray_sum():
    assert max_sequence([]) == 0
    assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
    assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155


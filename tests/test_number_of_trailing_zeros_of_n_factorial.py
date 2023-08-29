"""
No factorial is going to have fewer zeros than the factorial of a smaller
number.

Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
smaller than `n` (`n // 5`).

Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
of 25 smaller than n.

We continue on for all powers of 5 smaller than (or equal to) n.
"""


def zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count


def test_number_of_trailing_zeros_of_n_factorial():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    assert zeros(100000) == 24999

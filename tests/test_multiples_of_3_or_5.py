def is_multiple_of(multiple, num):
    return num % multiple == 0


def is_multiple_of_3(num):
    return is_multiple_of(3, num)


def is_multiple_of_5(num):
    return is_multiple_of(5, num)


def get_multiples(limit):
    return [x for x in range(1, limit) if is_multiple_of_3(x) or is_multiple_of_5(x)]


def solution(limit):
    return sum(get_multiples(limit))


def test_sum_multiples_of_3_or_5_below_given_number():
    assert solution(4) == 3
    assert solution(6) == 8
    assert solution(16) == 60
    assert solution(3) == 0
    assert solution(5) == 3
    assert solution(15) == 45
    assert solution(0) == 0
    assert solution(-1) == 0
    assert solution(10) == 23
    assert solution(20) == 78
    assert solution(200) == 9168

import statistics


def get_grade(*numbers):
    mean_value = statistics.mean(numbers)
    if mean_value >= 90:
        return "A"
    if mean_value >= 80:
        return "B"
    if mean_value >= 70:
        return "C"
    if mean_value >= 60:
        return "D"
    return "F"


def test_should_return_an_a():
    assert get_grade(95, 90, 93) == "A"
    assert get_grade(100, 85, 96) == "A"
    assert get_grade(92, 93, 94) == "A"
    assert get_grade(100, 100, 100) == "A"


def test_should_return_a_b():
    assert get_grade(70, 70, 100) == "B"
    assert get_grade(82, 85, 87) == "B"
    assert get_grade(84, 79, 85) == "B"


def test_should_return_a_c():
    assert get_grade(70, 70, 70) == "C"
    assert get_grade(75, 70, 79) == "C"
    assert get_grade(60, 82, 76) == "C"


def test_should_return_a_d():
    assert get_grade(65, 70, 59) == "D"
    assert get_grade(66, 62, 68) == "D"
    assert get_grade(58, 62, 70) == "D"


def test_should_return_a_f():
    assert get_grade(44, 55, 52) == "F"
    assert get_grade(48, 55, 52) == "F"
    assert get_grade(58, 59, 60) == "F"
    assert get_grade(0, 0, 0) == "F"

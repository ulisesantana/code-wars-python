from itertools import combinations


def choose_best_sum(max_distance, towns_to_visit, towns_distance_list):
    if len(towns_distance_list) < towns_to_visit:
        return None
    solutions = []
    for towns in combinations(towns_distance_list, towns_to_visit):
        distance = sum(towns)
        if distance == max_distance:
            return distance
        elif distance < max_distance:
            solutions.append(distance)
    return None if not solutions else max(solutions)


def test_best_travel():
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    assert choose_best_sum(230, len(xs) + 1, xs) is None
    assert choose_best_sum(230, 4, xs) == 230
    assert choose_best_sum(430, 5, xs) == 430
    assert choose_best_sum(430, 8, xs) is None

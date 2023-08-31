def exp_sum(n):
    limit = n + 1
    partitions = [0] * limit
    partitions[0] = 1

    for i in range(1, limit):
        for j in range(i, limit):
            partitions[j] += partitions[j - i]

    return partitions[n]


def test_explosive_sum():
    assert exp_sum(1) == 1
    assert exp_sum(2) == 2
    assert exp_sum(3) == 3
    assert exp_sum(4) == 5
    assert exp_sum(5) == 7
    assert exp_sum(10) == 42
    assert exp_sum(50) == 204226
    assert exp_sum(80) == 15796476
    assert exp_sum(100) == 190569292

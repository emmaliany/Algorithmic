from math import pow


def pythagorean_triplet_by_sum(sum: int) -> None:
    """
    print all pythagorean triplets that their sum is equal to param sum
    :param sum: int
    """
    a: int = 1
    b: int = 2
    c: int = sum - a - b

    while c > 2:
        while b > a:
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                print(f'{a}<{b}<{c}')
            a = a + 1
            b = b - 1
        a = 1
        c = c - 1
        b = sum - c - a


if __name__ == '__main__':
    pythagorean_triplet_by_sum(90)

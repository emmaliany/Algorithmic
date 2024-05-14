from math import log


def num_len(number: int) -> int:
    """
    find the length of a number
    :param number: int
    :return: int - returns the length of number param
    """
    return int(log(number, 10)) + 1


if __name__ == '__main__':
    print(num_len(1))

from mpmath import mp


def reverse_n_pi_digits(n: int) -> str:
    """
    return n (param) pi digits reversed
    :param n: int - determines how many digits of pi to return
    :return: str - returns n first digits of pi reversed as a string
    """
    mp.dps = n
    pi_sequence: str = str(mp.pi).replace('.', '')
    return pi_sequence[::-1]


if __name__ == '__main__':
    print(reverse_n_pi_digits(5))

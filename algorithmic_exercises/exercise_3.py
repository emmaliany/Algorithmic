from math import ceil


def is_palindrome(sequence: str) -> bool:
    """
    find if a string is palindrome
    :param sequence: str - the string the functions checks if palindrome
    :return: bool - returns if sequence param is palindrome
    """
    end_index: int = len(sequence) - 1
    middle: int = ceil(end_index / 2)

    for start_index in range(middle):
        if not sequence[start_index] == sequence[end_index]:
            return False
        end_index -= 1
    return True


def is_sorted_palindrome(sequence: str) -> bool:
    """
    find if a string is palindrome and if its in alphabetical order
    :param sequence: str - the string the functions checks if sorted palindrome
    :return: bool - returns if sequence param is sorted palindrome
    """
    if not is_palindrome(sequence):
        return False
    middle: int = ceil((len(sequence) - 1) / 2)
    for index in range(middle):
        if sequence[index] > sequence[index + 1]:
            return False
    return True


if __name__ == '__main__':
    print(is_sorted_palindrome('kayak'))

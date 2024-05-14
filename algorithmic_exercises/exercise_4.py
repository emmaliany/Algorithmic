import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def is_float(check: str) -> bool:
    """
    check if number in param can be typecast to float
    :param check: str
    :return: if param check can be cast to float
    """
    if check.count('.') > 1 or check.count('-') > 1:
        return False
    check = check.replace('.', '')
    check = check.replace('-', '')
    return check.isnumeric()


def show_pearson(numbers: list) -> None:
    """
    print on screen pearson correlation coefficient
    :param numbers: list - float list
    """
    x = np.array([*range(1, len(numbers) + 1)])
    y = np.array(numbers)

    if len(x) < 2:
        print('cannot calculate pearson correlation coefficient')
        return
    print(f'Pearson Correlation Coefficient: \n\t'
          f'The value of R is: {stats.pearsonr(x, y)[0]}\n\t'
          f'The p-value is: {stats.pearsonr(x, y)[1]}')


def create_graph(numbers: list) -> None:
    """
    show graph of numbers in numbers list
    :param numbers: list - float list
    """
    title_font = {'family': 'serif', 'color': 'magenta', 'size': 20}
    label_font = {'family': 'serif', 'color': 'darkred', 'size': 15}

    x = np.array([*range(1, len(numbers) + 1)])
    y = np.array(numbers)
    plt.scatter(x, y)
    plt.title("ALL NUMBERS", fontdict=title_font)
    plt.xlabel("order of appearance", fontdict=label_font)
    plt.ylabel("numbers", fontdict=label_font)
    plt.xticks(x)
    plt.grid()

    plt.show()


def series_of_numbers() -> None:
    """
    get numbers (float) from user and:
    print average, positive numbers counter, all numbers sorted
    show graph of numbers as a function of appearance
    print pearson correlation coefficient r,p values
    """
    numbers: list = []
    numbers_sum: float = 0
    positive_counter: int = 0
    while True:
        number = input('enter wanted numbers. when done enter -1: ')
        if number == '-1':
            break
        if not is_float(number):
            print('input must be a number, please try again')
            continue
        number = float(number)
        numbers.append(number)
        numbers_sum += number
        if number > 0:
            positive_counter += 1

    if len(numbers) == 0:
        print(f'the average is 0')
    else:
        print(f'the average is: {numbers_sum / len(numbers)}')
    print(f'there were {positive_counter} positive numbers')
    print(sorted(numbers))

    create_graph(numbers)
    show_pearson(numbers)


if __name__ == '__main__':
    series_of_numbers()

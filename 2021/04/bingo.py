## Solution AOC21 Day 4
## Maximilian Jalea

import numpy as np


def myint(i):
    try:
        output = int(i)
    except:
        output = None
    return output


def read_input(path):
    with open(path, 'r') as file:
        document = file.read()
        lines = document.split("\n")

    numbers = list(map(int, lines[0].split(",")))
    bingo = np.zeros(((len(lines[1:])) // 6, 5, 5))
    for i, line in enumerate(lines[1:]):
        elements = list(map(myint, line.split(" ")))
        while len(elements) > 5:
            elements.remove(None)
        bingo[i // 6, (i % 6) - 1] = np.array(elements)
    return numbers, bingo


def find_bingo(sheets):
    sum_one = np.sum(sheets, axis=1)
    sum_two = np.sum(sheets, axis=2)
    min_one = np.min(sum_one)
    min_two = np.min(sum_two)
    if min_one == 0:
        found_sheet = np.unravel_index(np.argmin(sum_one), sum_one.shape)[0]
    elif min_two == 0:
        found_sheet = np.unravel_index(np.argmin(sum_two), sum_two.shape)[0]
    else:
        found_sheet = None

    return found_sheet


def run_bingo(numbers, sheets):
    found_sheets = np.ones_like(sheets)
    for number in numbers:
        found_sheets[sheets == number] = 0
        found_sheet = find_bingo(found_sheets)
        if found_sheet is not None:
            return sheets[found_sheet], found_sheets[found_sheet], number
    return None


def cal_score(sheet, marked, last_number):
    unmarked_sum = np.sum(np.multiply(sheet, marked))
    return unmarked_sum * last_number


def find_last(numbers, sheets):
    found_sheets = np.ones_like(sheets)
    sheet_win = np.zeros(sheets.shape[0])
    for i, number in enumerate(numbers):
        found_sheets[sheets == number] = 0
        sum_one = np.sum(found_sheets, axis=1)
        sum_two = np.sum(found_sheets, axis=2)
        sheet_win[np.sum((sum_one == 0), axis=1) > 0] = 1
        sheet_win[np.sum((sum_two == 0), axis=1) > 0] = 1
        if np.sum(sheet_win) >= 99:
            last_sheet = np.argmin(sheet_win)
            return sheets[last_sheet]
    return None


if __name__ == '__main__':
    input_path = "./input.txt"
    numbers, bingo = read_input(input_path)

    sheet, marked, last_number = run_bingo(numbers, bingo)
    score = cal_score(sheet, marked, last_number)
    print(f"Final score of best board: {score}")

    sheet = find_last(numbers, bingo)
    sheet, marked, last_number = run_bingo(numbers, sheet[np.newaxis, :, :])
    score = cal_score(sheet, marked, last_number)
    print(f"Final score of last board: {score}")
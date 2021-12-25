## Solution AOC21 Day 4
## Maximilian Jalea

import numpy as np


def read_input(path):
    with open(path, 'r') as file:
        document = file.read()
        lines = document.split("\n")
    operations = []
    for line in lines:
        items = line.split(" -> ")
        coords_one = list(map(int, items[0].split(",")))
        coords_one.extend(list(map(int, items[1].split(","))))
        operations.append(coords_one)
    return np.array(operations)


def easy_lines(operations):
    maximums = np.max(operations, axis=0)
    max_x = np.max([maximums[0], maximums[2]])
    max_y = np.max([maximums[1], maximums[3]])
    map = np.zeros((max_x + 1, max_y + 1))
    for operation in operations:
        if operation[0] == operation[2]:
            if operation[1] < operation[3]:
                map[operation[0], operation[1]:(operation[3] + 1)] += 1
            else:
                map[operation[0], operation[3]:(operation[1] + 1)] += 1
        elif operation[1] == operation[3]:
            if operation[0] < operation[2]:
                map[operation[0]:(operation[2] + 1), operation[1]] += 1
            else:
                map[operation[2]:(operation[0] + 1), operation[1]] += 1
    return map


def more_lines(operations):
    maximums = np.max(operations, axis=0)
    max_x = np.max([maximums[0], maximums[2]])
    max_y = np.max([maximums[1], maximums[3]])
    map = np.zeros((max_x + 1, max_y + 1))
    for operation in operations:
        if operation[0] == operation[2]:
            if operation[1] < operation[3]:
                map[operation[0], operation[1]:(operation[3] + 1)] += 1
            else:
                map[operation[0], operation[3]:(operation[1] + 1)] += 1
        elif operation[1] == operation[3]:
            if operation[0] < operation[2]:
                map[operation[0]:(operation[2] + 1), operation[1]] += 1
            else:
                map[operation[2]:(operation[0] + 1), operation[1]] += 1
        else:
            if operation[0] < operation[2]:
                if operation[1] < operation[3]:
                    for i in range(operation[2] - operation[0] + 1):
                        map[operation[0] + i, operation[1] + i] += 1
                else:
                    for i in range(operation[2] - operation[0] + 1):
                        map[operation[0] + i, operation[1] - i] += 1
            else:
                if operation[1] > operation[3]:
                    for i in range(operation[0] - operation[2] + 1):
                        map[operation[0] - i, operation[1] - i] += 1
                else:
                    for i in range(operation[0] - operation[2] + 1):
                        map[operation[0] - i, operation[1] + i] += 1
    return map


if __name__ == '__main__':
    input_path = "./input.txt"
    operations = read_input(input_path)
    finished_map = easy_lines(operations)
    print(f"Horizontal and Vertical: {np.sum(finished_map>=2)}")

    finished_map = more_lines(operations)
    print(f"Plus Diagonal: {np.sum(finished_map>=2)}")
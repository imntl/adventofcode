## Solution AOC21 Day 3
## Maximilian Jalea


def read_input(path):
    with open(path, 'r') as file:
        document = file.read()
        lines = document.split("\n")[:-1]
    return lines


def get_numbers(inputs):
    numbers = [0] * len(inputs[0])
    for report in inputs:
        for i, number in enumerate(report):
            numbers[i] += int(number)
    return numbers


def get_rates(inputs):
    gamma_rate = ""
    epsilon_rate = ""
    numbers = get_numbers(inputs)

    for number in numbers:
        if number >= (len(inputs) / 2):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return gamma_rate, epsilon_rate


def get_other_rates(inputs, oxygen=True):
    for i in range(len(inputs[0])):
        if len(inputs) == 1: return inputs[0]
        numbers = get_numbers(inputs)
        if oxygen:
            binary = "1" if numbers[i] >= (len(inputs) / 2) else "0"
        else:
            binary = "0" if numbers[i] >= (len(inputs) / 2) else "1"
        new_inputs = []
        for report in inputs:
            if report[i] == binary:
                new_inputs.append(report)
        inputs = new_inputs
        print(i, len(inputs))

    return inputs[0]


if __name__ == '__main__':
    input_path = "./input.txt"
    inputs = read_input(input_path)

    gamma_rate, epsilon_rate = get_rates(inputs)
    gamma, epsilon = int(gamma_rate, 2), int(epsilon_rate, 2)
    print(
        f"The power consuption is {gamma * epsilon} with rates {gamma} and {epsilon}."
    )
    oxygen_rate = get_other_rates(inputs)
    scrubber_rate = get_other_rates(inputs, oxygen=False)
    oxygen, scrubber = int(oxygen_rate, 2), int(scrubber_rate, 2)
    print(
        f"The life support rating is {oxygen * scrubber} with rates {oxygen} and {scrubber}."
    )

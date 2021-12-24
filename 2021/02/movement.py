## Solution AOC21 Day 2
## Maximilian Jalea

def read_input(path):
    with open(path, 'r') as file:
        document = file.read()
        lines = document.split("\n")[:-1]
    return lines
    
def easy_movement(inputs):
    horizontal = 0
    depth = 0

    for move in inputs:
        command, length = move.split(" ")
        if command == "forward":
            horizontal += int(length)
        elif command == "down":
            depth += int(length)
        elif command == "up":
            depth -= int(length)
        else:
            print(f"Command {command} not found!")

    return (horizontal, depth)

def complicated_movement(inputs):
    horizontal = 0
    depth = 0
    aim = 0

    for move in inputs:
        command, length = move.split(" ")
        if command == "forward":
            horizontal += int(length)
            depth += int(length) * aim
        elif command == "down":
            aim += int(length)
        elif command == "up":
            aim -= int(length)
        else:
            print(f"Command {command} not found!")

    return (horizontal, depth)

if __name__ == '__main__':
    input_path = "./input.txt"
    inputs = read_input(input_path)

    horizontal, depth = easy_movement(inputs)
    print(f"Multiplied position is {horizontal * depth}, with Horizontal of {horizontal} and Depth of {depth}")

    horizontal, depth = complicated_movement(inputs)
    print(f"Multiplied position is {horizontal * depth}, with Horizontal of {horizontal} and Depth of {depth}")

## Solution AOC21 Day 1
## Maximilian Jalea

def read_input(path):
    with open(path, 'r') as file:
        document = file.read()
        lines = document.split("\n")[:-1]
    return list(map(int, lines))
    
def easy_increase(input):
    increased = 0
    
    for a,b in zip(inputs[0:-1], inputs[1:]):
        if a < b: increased += 1
    return increased

def three_increase(input):
    increased = 0

#199  A      
#200  A B       -> Same for both three-inputs A & B
#208  A B       -> Same for both three inputs A & B
#210    B 

# Looking at the example input, one can see, that the last two of the first and
# the first two of the second input is the same, so when summing, we do not
# need to use them and only compare the first of the first three-input and the
# last of the second three-input. 

    for a,b in zip(inputs[0:-3], inputs[3:]):
        if a < b: increased += 1
    return increased


    return increased

if __name__ == '__main__':
    input_path = "./input.txt"
    inputs = read_input(input_path)

    easy_increased = easy_increase(inputs)
    print(f"There are {easy_increased} measurements that are larger than the previous.")

    three_increased = three_increase(inputs)
    print(f"There are {three_increased} measurements with summing that are larger than the previous.")

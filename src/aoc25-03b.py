'''
Advent of Code 2025: https://adventofcode.com/

Day X: title: https://adventofcode.com/2025/day/3
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-03
'''

def parse_input(filename):
    banks = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            banks.append(line.strip())
    return banks

def activate_bank(bank:str, size:int)->int:
    '''
    for an approach with 12 activations, I go digit by digit, looking for the max of possible remaining numbers
    '''
    max_joltage=0
    battery_index=0
    print(f"--->{bank}")
    for i in range(size):
        battery_joltage = max([int(x) for x in bank[battery_index:len(bank)-(size-i)+1]])
        max_joltage+=battery_joltage*(10**(size-i-1))
        battery_index += bank[battery_index:].index(str(battery_joltage))
        print(f"{i} Joltage {battery_joltage} found at {battery_index}")
        battery_index +=1
    print(f"Max joltage: {max_joltage}")
    return max_joltage

def main():
    banks = parse_input("data/input-03.txt")
    result = 0
    for bank in banks:
        result+=activate_bank(bank,12)
    print(result)

if __name__ == '__main__':
    main()


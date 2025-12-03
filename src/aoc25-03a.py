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

def activate_bank(bank:str)->int:
    max_joltage=0
    for i1 in range(len(bank)-1):
        for i2 in range(i1+1, len(bank)):
            joltage = int(bank[i1]+bank[i2])
            max_joltage = max(max_joltage, joltage)
    print(f"Max joltage: {max_joltage}")
    return max_joltage

def main():
    banks = parse_input("data/input-03.txt")
    result = 0
    for bank in banks:
        result+=activate_bank(bank)
    print(result)

if __name__ == '__main__':
    main()


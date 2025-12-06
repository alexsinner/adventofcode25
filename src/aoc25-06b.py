'''
Advent of Code 2025: https://adventofcode.com/

Day 6: trash compactor: https://adventofcode.com/2025/day/6
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-06
'''
from matrix import Matrix
import math

def parse_input(filename):
    problems = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            # add a space to the end to make sure we add the final result
            problems.append(line[-2::-1]+" ")
    return problems

def main():
#    input = parse_input("data/input-06.txt")
    input = parse_input("data/test-06.txt")
    print(input)
    grand_total = 0
    values = []
    for col in range(len(input[0])):
        value = ''.join([input[x][col] for x in range(len(input)-1)])
        if input[-1][col] in {'*','+'}:
            operand = input[-1][col]
            print(f"New operand: {operand}")
        if value.strip()=='':
            print(f"New empty column")
            if operand == '+':
                print(f"Adding +{sum(values)}")
                grand_total += sum(values)
            elif operand == '*':
                print(f"Adding *{math.prod(values)}")
                grand_total += math.prod(values)
            else:
                print("ERROR: bad operand")
                pass
            values = []
        else:
            print(f"New value: {value}")
            values.append(int(value))
    print(grand_total)
            
if __name__ == '__main__':
    main()


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
            problems.append(line.split())
    return problems

def main():
    input = parse_input("data/input-06.txt")
    grand_total = 0
    for col in range(len(input[0])):
        values = [int(input[x][col]) for x in range(len(input)-1)]
        operand = input[-1][col]
        result = 0
        if operand == '+':
            result = sum(values)
        elif operand == '*':
            result = math.prod(values)
        else:
            pass
        grand_total += result
    print(grand_total)

if __name__ == '__main__':
    main()


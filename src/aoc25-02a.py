
'''
Advent of Code 2025: https://adventofcode.com/

Day 2: : https://adventofcode.com/2025/day/2

Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-02
'''

import math

def parse_input(filename):
    ranges = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            for r in line.strip().split(','):
                (first_id, last_id) = tuple(r.split('-'))
                ranges.append([first_id, last_id])
    return ranges

def evaluate_range(first_id:str, last_id:str)->int:
    '''check how many invalid ids are in the given range, and return the sum of all invalid ids'''
    result = 0
    if len(first_id)%2 == 1:
        # odd size, so need to start with the next highest power of 10
        start_eval = int(math.pow(10, math.floor((len(first_id)/2))))
    else:
        start_eval = int(first_id[:len(first_id)//2])
    if len(last_id)%2 ==1:
        # odd size, so need to end with a lower power of 10
        end_eval = int(math.pow(10, len(last_id)//2))-1
    else:
        end_eval = int(last_id[:len(last_id)//2])
    print(f"Evaluating range {first_id}-{last_id}, starting with {start_eval}, ending with {end_eval}")

    for x in range(start_eval, end_eval+1):
        invalid_id = int(str(x)+str(x))
        if invalid_id >= int(first_id) and invalid_id <= int(last_id):
            result+=invalid_id
            print(f"Invalid ID: {invalid_id}")
    return result

def main():
    result = 0
#    ranges = parse_input("data/test-02.txt")
    ranges = parse_input("data/input-02.txt")
    for r in ranges:
        result += evaluate_range(r[0],r[1])
    print(result)    

if __name__ == '__main__':
    main()


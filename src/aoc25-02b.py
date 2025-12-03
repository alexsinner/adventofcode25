
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
    print(f"Evaluating range {first_id}-{last_id}")
    invalid_ids = set()
    # First calculate the set of possible pattern lengths for invalid ids (e.g. 1, 2, 3 for a length of 12)
    # keep in mind that first_id may have a different length than last_id
    repeat_lengths = {1}
    for x in range(2, len(last_id)//2+1): # check for each number between 2 and half length of the longer id
        if len(first_id)%x == 0 or len(last_id)%x ==0:
            repeat_lengths.add(x)
#    print(f"Repeat lengths for range {first_id}-{last_id}: {repeat_lengths}")
    for l in repeat_lengths:
        # now we need to generate the invalid patterns 
        # first determine the start pattern 
        # if the end id is an order of magnitude larger, I am picking a broader set of patterns. There is probably a way to be more precise, but I am lazy
        if len(last_id) > len(first_id):
            start_pattern = 10**(l-1)
            end_pattern = 10**l-1
        elif len(first_id)%l == 0 and len(last_id)%l ==0:
            start_pattern = first_id[:l]
            end_pattern = last_id[:l]
        else: 
            # This should not happen
            print("ERROR - the end id should be larger or equal to the start id")
#        print(f"Start pattern: {start_pattern}")
#        print(f"End pattern: {end_pattern}")
        #now iterate over all the patterns
        # first identify all the id_lengths
        id_lengths = range(len(first_id),len(last_id)+1)
        for p in range(int(start_pattern), int(end_pattern)+1):
            for il in id_lengths:
                # there need to be at least 2 repeats
                if il%len(str(p))==0 and il//len(str(p))>=2: 
                    invalid_id = ''.join([str(p) for i in range(il//len(str(p)))])
                    if int(invalid_id) >= int(first_id) and int(invalid_id) <= int(last_id): 
                        invalid_ids.add(int(invalid_id))
    result=0
    for ii in invalid_ids:
        print(f"Invalid ID: {ii}")
        result+=ii
    return result

def main():
    result = 0
    ranges = parse_input("data/test-02.txt")
#    ranges = parse_input("data/input-02.txt")
    for r in ranges:
        result += evaluate_range(r[0],r[1])
    print(result)    

if __name__ == '__main__':
    main()


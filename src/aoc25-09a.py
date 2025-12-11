'''
Advent of Code 2025: https://adventofcode.com/

Day 9: Movie Theater: https://adventofcode.com/2025/day/9
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-09
'''

def rectangle_size(a,b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

def compute_largest_rectangle(tilelist):
    max_rectangle = 0
    for i, t1 in enumerate(tilelist[:-2]):
        for t2 in tilelist[i+1:]:
            max_rectangle = max(max_rectangle, rectangle_size(t1,t2))
    return max_rectangle

def parse_input(filename):
    tiles = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            tiles.append(tuple([int(x) for x in line.split(',')]))
    return tiles

def main():
    input = parse_input("data/input-09.txt")
    max_rectangle = compute_largest_rectangle(input)
    print(max_rectangle)

if __name__ == '__main__':
    main()


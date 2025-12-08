'''
Advent of Code 2025: https://adventofcode.com/

Day 8: Playground: https://adventofcode.com/2025/day/8
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-08
'''
import math

def parse_input(filename):
    junction_boxes = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            junction_boxes.append(tuple([int(x) for x in line.split(',')]))
    return junction_boxes

def distance(a, b):
    distance = sum([(b[i]-a[i])**2 for i in range(len(a))])
    return math.sqrt(distance)

def compute_distances(junction_boxes):
    distances = []
    junction_boxes.sort()
    for (i, jb1) in enumerate(junction_boxes[:-2]):
        for jb2 in junction_boxes[i+1:]:
            distances.append((jb1, jb2, distance(jb1, jb2)))
    return sorted(distances, key=lambda x: x[2])

def compute_circuits(distances, max_connections=10):
    circuits = []
    merged_circuits = []
    for (jb1, jb2, distance) in distances[:max_connections]:
        circuits.append(set([jb1, jb2]))
    # now let's merge all circuits that can be merged
    while len(circuits) >0:
        c = circuits.pop(0)
        is_merged=False
        for c2 in circuits.copy():
            if not (c.isdisjoint(c2)):
                # merging
                is_merged=True
                merged = c.union(c2)
                circuits.remove(c2)
                if merged not in circuits:
                    circuits.append(merged)                
        if not is_merged:
            merged_circuits.append(c)
    return merged_circuits

def main():
    junction_boxes = parse_input("data/test-08.txt")
#    junction_boxes = parse_input("data/input-08.txt")
    distances = compute_distances(junction_boxes)
    merged_circuits = compute_circuits(distances, 1000)
    result = math.prod(sorted([len(x) for x in merged_circuits], reverse=True)[:3]) 
    print(result)

if __name__ == '__main__':
    main()


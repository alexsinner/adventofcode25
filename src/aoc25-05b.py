'''
Advent of Code 2025: https://adventofcode.com/

Day 5: title: https://adventofcode.com/2025/day/5
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-05
'''

def parse_input(filename):
    ranges = []
    ingredients = []
    with open(filename, 'r') as f:
        parse_ranges=True
        for line in f.readlines():
            if parse_ranges:
                if line.strip()=='':
                    parse_ranges=False
                    continue
                else:
                    range = tuple([int(x) for x in line.split('-')])
                    ranges.append(range)
            else:
                ingredients.append(int(line))
            pass
    return sorted(ranges), sorted(ingredients)

def consolidate_ranges(ranges):
    # take a list of ranges and return a new list of ranges without any overlaps
    # first, identify all overlaps by storing a list of overlaps for each range
    consolidated_ranges = []
#    print(f"Ranges: {ranges}")
    while len(ranges) >0:
        r1 = ranges.pop(0)
        has_overlaps = False
#        print(f"---checking {r1}")
        for r2 in ranges:
#            print(f"---against {r2}")
            if ((r1[0] >= r2[0] and r1[0] <= r2[1]) or (r1[1] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[0] <= r1[1]) or (r2[1] >= r1[0] and r2[1] <= r1[1])):
                consolidated_range=(min(r1[0],r2[0]), max(r1[1],r2[1]))
                if not consolidated_range in ranges:
                    ranges.append(consolidated_range)
#                 print(f"Consolidated {r1} and {r2} into {consolidated_range}")
#                else:
#                  print(f"Known consolidated range: {consolidated_range}")
                has_overlaps = True
            else:
#               print(f"No overlap")
                pass
        # after checking all other elements, if there was no overlap we can add it to the new set of overlaps
        if not has_overlaps:
#            print(f"Adding {r1} to consolidated ranges")
            consolidated_ranges.append(r1)
#    print(f"Consolidated ranges: {consolidated_ranges}")
    return consolidated_ranges


def main():
    ranges, ingredients = parse_input("data/input-05.txt")
#    ranges, ingredients = parse_input("data/test-05.txt")
    consolidated = consolidate_ranges(ranges)
    result = sum((r[1]-r[0]+1) for r in consolidated )
    print(result)

if __name__ == '__main__':
    main()


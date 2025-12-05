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

def main():
    ranges, ingredients = parse_input("data/input-05.txt")
#    ranges, ingredients = parse_input("data/test-05.txt")
    print(f"Ranges: {ranges} \n\nIngredients: {ingredients} ")
    result = 0
    for id in ingredients:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                print(f"fresh id: {id} in range {range}")
                result+=1
                break
            else:
                continue
    print(result)

if __name__ == '__main__':
    main()


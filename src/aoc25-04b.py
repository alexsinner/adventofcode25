'''
Advent of Code 2025: https://adventofcode.com/

Day X: title: https://adventofcode.com/2025/day/4
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-04
'''

from matrix import Matrix

class Floor(Matrix):

    def is_position_accessible(self, x, y)->bool:
        if self.is_out_of_bounds((x,y)):
            return False
        if self.get(x,y) != '@':
            return False
        else:
            paperrollcount=0
            neighbors = self.get_neighbors(x,y,True)
            for n in neighbors:
                # now we immediately remove any paperrolls - no longer necessary to treat removables as rolls
                if self.get(n[0],n[1]) == '@':
                    paperrollcount+=1
            if paperrollcount <4:
                self.set(x, y, 'x')
                return True
            else:
                return False

def parse_input(filename):
    floorplan = Floor.from_inputfile(filename)
    return floorplan

def main():
    input = parse_input("data/input-04.txt")
    result = 0
    stopcondition = True
    while stopcondition:
        stopcondition = False
        for x in range(input.width):
            for y in range(input.height):
                if input.is_position_accessible(x, y):
                    print(f"position {x}, {y} with value {input.get(x,y)} is accessible, removing roll")
                    result+=1
                    stopcondition=True

    input.visualize()    

    print(result)

if __name__ == '__main__':
    main()


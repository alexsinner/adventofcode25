'''
Advent of Code 2025: https://adventofcode.com/

Day 7: Laboratories: https://adventofcode.com/2025/day/7
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-07
'''

from matrix import Matrix

class TachyonManifold(Matrix):

    START = 'S'
    EMPTY = '.'
    SPLITTER = '^'
    BEAM = '|'

    def compute_timelines(self):
        # first initialize all empty fields to 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x,y)==self.EMPTY:
                    self.set(x,y, 0)
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x,y)==self.START:
                    self.set(x, y+1, 1)
                elif self.get(x,y)==self.SPLITTER:
                    self.set(x-1,y, self.get(x-1,y) + self.get(x,y-1))
                    self.set(x+1,y, self.get(x+1,y) + self.get(x,y-1))
                else:
                    if isinstance(self.get(x,y-1), int):
                        self.set(x,y, self.get(x,y)+self.get(x,y-1))
        self.visualize()
        return sum(self.matrix[self.height-1])

    def visualize(self):
        for y in self.matrix:
            print(''.join([str(x) for x in y]))

def main():
#    input = TachyonManifold.from_inputfile("data/input-07.txt")
    input = TachyonManifold.from_inputfile("data/test-07.txt")
    beams = input.compute_timelines()
    print(beams)

if __name__ == '__main__':
    main()


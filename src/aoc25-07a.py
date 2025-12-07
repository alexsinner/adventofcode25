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

    def compute_split_beams(self):
        self.direction = self.DOWN
        for x in range(len(self.matrix[0])):
            if self.matrix[0][x] == self.START:
                self.position = (x, 0)
        # now let's find all splits. we do this with some breadth first search 
        splits = set()
        beamqueue = [self.position]
        while len(beamqueue) > 0:
            pos = beamqueue.pop(0)
            (x, y) = (pos[0], pos[1])
            if self.get(x, y) == self.SPLITTER:
                splits.add(pos)
                left_beam = (x + self.LEFT[0], y + self.LEFT[1])
                right_beam = (x + self.RIGHT[0], y + self.RIGHT[1])
                if not self.is_out_of_bounds(left_beam) and left_beam not in beamqueue:
                    beamqueue.append(left_beam)
                if not self.is_out_of_bounds(right_beam) and right_beam not in beamqueue:
                    beamqueue.append(right_beam)
            else:
                down_beam = (x + self.DOWN[0], y + self.DOWN[1])
                if not self.is_out_of_bounds(down_beam):
                    beamqueue.append(down_beam)
        return len(splits)

def main():
    input = TachyonManifold.from_inputfile("data/input-07.txt")
    print(input.compute_split_beams())

if __name__ == '__main__':
    main()


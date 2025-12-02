'''
Advent of Code 2025: https://adventofcode.com/

Day 1: secret entrance: https://adventofcode.com/2025/day/1
'''

class Safe():
    '''
    The safe has a dial with an initial position that can be turned either right or left.
    '''
    def __init__(self, dial_size=100, dial_position=50):
        self.dial_size = dial_size
        self.dial_position = dial_position

    def rotate(self, direction, steps) -> (int, bool):
        '''
        rotates the dial either right (R) or left (L) and returns a tuple (dial_position, is_on_0)
        '''
        if direction == 'R':
            self.dial_position = (self.dial_position + steps) % self.dial_size
        elif direction == 'L':
            self.dial_position = (self.dial_position - steps) % self.dial_size
        else:
            print("ERROR - wrong instruction")
        return (self.dial_position, self.dial_position==0)

def main():
    f = open("data/input-01a.txt", "r")
    lines = f.read().splitlines()
    f.close()
    safe = Safe()
    result = 0
    for l in lines:
        (_, is_zero) = safe.rotate(l[0], int(l[1:]))
        result+= is_zero
    print(result)    

if __name__ == '__main__':
    main()


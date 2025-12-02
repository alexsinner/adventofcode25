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
        rotates the dial either right (R) or left (L) and returns a tuple (dial_position, number of times it passes 0)
        '''
        ## first check how often you will pass 0
        passes = steps // self.dial_size
        ## remaining steps
        steps = steps % self.dial_size
        initial_position = self.dial_position
        if direction == 'R':
            self.dial_position = (self.dial_position + steps) % self.dial_size
            if initial_position != 0 and (self.dial_position < initial_position or self.dial_position ==0): 
                passes+=1
        elif direction == 'L':
            self.dial_position = (self.dial_position - steps) % self.dial_size
            if initial_position != 0 and (self.dial_position > initial_position or self.dial_position ==0): 
                passes+=1
        else:
            print("ERROR - wrong instruction")
        print(f"POS {initial_position} - {direction}{steps} - POS {self.dial_position} - PASSES {passes}")
        return (self.dial_position, passes)

def main():
#    f = open("data/test-01.txt", "r")
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


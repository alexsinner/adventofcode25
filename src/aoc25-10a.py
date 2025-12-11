'''
Advent of Code 2025: https://adventofcode.com/

Day 10: Factory: https://adventofcode.com/2025/day/10
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-10
'''

from bitarray import bitarray
from heapq import *
#import re

class Machine():

    def __init__(self, indicator_lights:str, button_wirings:[], joltage:str):
        self.target_light_pattern = self.parse_light_pattern(indicator_lights)
        # set the lights state to a bit array of same size as the target pattern where all lights are initially off
        self.lights = bitarray(len(self.target_light_pattern))
        self.lights[:] = False 
        self.button_wirings=[]
        for bw in button_wirings:
            self.button_wirings.append(self.parse_button_wiring(bw, len(self.lights)))
        # not needed yet, so will not parse
        self.joltage = joltage

    def parse_light_pattern(self, pattern:str):
        return bitarray(pattern[1:-1].replace('.', '0').replace('#', '1'))

    def parse_button_wiring(self, wiring:tuple, length:int):
        '''
        Turn button wirings in the form of a tuple (pos1, pos2, ...) into a bitarray
        Example for a bitarray of length 5
        (2, 4) -> '00101'
        '''
        w_bitarray = bitarray(length)
        for b in wiring:
            w_bitarray[b] = True
        return w_bitarray

    def __str__(self):
        return(f"###Current State: {self.lights}###\nTarget Pattern: {self.target_light_pattern}\nButton Wirings: {self.button_wirings}\nJoltage: {self.joltage}")

    def configure(self):
        state = self.target_light_pattern
        presses = 0
        queue = []
        for button in self.button_wirings:
            heappush(queue, (presses+1, state ^ button, button))
        while state != self.lights:
            (p, s, b) = heappop(queue)
            state = s
            presses = p
            for button in self.button_wirings:
                if button != b:
                    heappush(queue, (p+1, s ^ button, button))
        return presses            

    @classmethod
    def from_line(cls, line):
        elements = line.split(' ')
        indicator_pattern = elements[0]
        joltage = elements[-1]
        button_wirings = []
        for bw in elements[1:-1]:
            w_tuple = tuple(int(x) for x in bw[1:-1].split(','))
            button_wirings.append(w_tuple)
        return(cls(indicator_pattern, button_wirings, joltage))

def parse_input(filename):
    machines = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            machines.append(Machine.from_line(line))
    return machines

def main():
    machines = parse_input("data/input-10.txt")
    result = 0
    for machine in machines:
        result+=machine.configure()
    print(result)

if __name__ == '__main__':
    main()


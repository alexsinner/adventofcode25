'''
Advent of Code 2025: https://adventofcode.com/

Day 11: Reactor: https://adventofcode.com/2025/day/11
Author: Alex Sinner <alex@sinner.lu>
Date: 2025-12-11
'''

def parse_input(filename):
    machines = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            ls1 = line.split(':')
            left = ls1[0]
            out = ls1[1].strip().split(' ')
            machines[left]=out
    return machines

def count_paths(machines):
    path_count=0
    visited_nodes = set()
    queue = [('you', visited_nodes)]
    while len(queue)>0:
        node, visited = queue.pop()
        new_visited = set(visited)
        new_visited.add(node)
        if node == 'out':
            path_count+=1
        else:
            for out in machines[node]:
                if not out in visited_nodes:
                    queue.append((out, new_visited))
    return path_count

def main():
    machines = parse_input("data/input-11.txt")
    result = count_paths(machines)
    print(result)

if __name__ == '__main__':
    main()


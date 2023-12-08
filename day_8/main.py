TEST = "day_8/test.txt"
DATA = "day_8/data.txt"

import re
from itertools import cycle


def read_file(file):
    with open(file=file, mode="r") as file:
        return file.read()

content = read_file(DATA).strip().splitlines()

directions = []
for char in content[0]:
    directions.append(char)

directions_cycle = cycle(directions)

map = {}
for line in content[2:]:
    pattern = r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)'
    match = re.match(pattern, line)
    NODE, LEFT, RIGHT = match.groups()
    map[NODE] = {
            'L': LEFT,
            'R': RIGHT
            }

node = 'AAA'
steps = 0
while node != 'ZZZ':
    turn = next(directions_cycle)
    steps += 1
    node = map[node][turn]

print(steps)

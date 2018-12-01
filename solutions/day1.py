import itertools

from aocd import data
from utils import timed

input = [int(i) for i in data.split()]

@timed
def part_one(deltas):
    return sum(deltas)

@timed
def part_two(deltas):
    frequency = 0
    seen = set([frequency]) # 0 can be repeated
    for delta in itertools.cycle(deltas):
        frequency += delta
        if frequency in seen:
            return frequency
        seen.add(frequency)

print(part_one(input))
print(part_two(input))

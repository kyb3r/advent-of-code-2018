import itertools

from aocd import data
from utils import timed

input = [int(i) for i in data.split('\n')]

@timed
def part_one(deltas):
    return sum(deltas)

@timed
def part_two(deltas):
    seen = set()
    frequency = 0
    for delta in itertools.cycle(deltas):
        frequency += delta
        if frequency in seen:
            return frequency
        seen.add(frequency)

print(part_one(input))
print(part_two(input))
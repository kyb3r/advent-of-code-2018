from aocd import data
from utils import timed
import itertools

input = data.split()

@timed
def part_one(boxes):
    twice = 0
    thrice = 0
    for box in boxes:
        twice += any(box.count(letter) == 2 for letter in box)
        thrice += any(box.count(letter) == 3 for letter in box)
    checksum = twice * thrice 
    return checksum


@timed
def part_one(boxes):
    """Shorter version, but harder to understand"""
    f = lambda c: sum(any(b.count(l) == c for l in b) for b in boxes) 
    return f(2) * f(3)

@timed
def part_two(boxes):
    for x, y in itertools.combinations(boxes, 2):
        difference = [i for i, l in enumerate(x) if y[i] != l]
        if len(difference) == 1:
            index = difference[0]
            return x[:index] + x[index+1:]

print(part_one(input))
print(part_two(input))
from aocd import data
from utils import timed

input = data.split()

@timed
def part_one(boxes):
    twice = 0
    thrice = 0
    for box in boxes:
        twice += any(box.count(x) == 2 for x in box)
        thrice += any(box.count(x) == 3 for x in box)
    checksum = twice * thrice 
    return checksum

@timed
def part_two(boxes):
    for x in boxes:
        for y in boxes:
            difference = [i for i, l in enumerate(x) if y[i] != l]
            if len(difference) == 1:
                index = difference[0]
                return x[:index] + x[index+1:]

print(part_one(input))
print(part_two(input))
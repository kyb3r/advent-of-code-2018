from aocd import data
from collections import defaultdict
from dataclasses import dataclass
import re

@dataclass
class Claim:
    """Represents a claim"""
    id: int 
    x: int
    y: int 
    width: int 
    height: int 

    def __hash__(self):
        return self.id

    @property
    def area(self):
        return self.width * self.height


claims = map(lambda s: Claim(*map(int, re.findall(r'\d+', s))), data.split('\n'))
grid = defaultdict(set)

def part_one(claims):
    for claim in claims:
        for r in range(claim.x, claim.x + claim.width):
            for c in range(claim.y, claim.y + claim.height):
                grid[(r,c)].add(claim)

    return len([k for k, v in grid.items() if len(v) > 1])

def part_two(grid):
    possible = defaultdict(int)
    for cell, claims in grid.items():
        if len(claims) == 1:
            sol = claims.pop()
            possible[sol] += 1 # could be part of a larger claim that is actually already intersected
    return next(k for k, v in possible.items() if k.area == v).id

print(part_one(claims))
print(part_two(grid))
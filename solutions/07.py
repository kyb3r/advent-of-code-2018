from dataclasses import dataclass, field
import functools
import re

from aocd import data
from utils import timed

def memoized(cls):
    cls.cache = cache = {}
    @functools.wraps(cls)
    def wrapper(letter):
        if letter not in cache:
            cache[letter] = cls(letter)
        return cache[letter]
    return wrapper

@memoized
@dataclass
class Step:
    letter: str
    executed: bool = False
    before: list = field(default_factory=list)

    @property
    def ready(self):
        for step in self.cache.values():
            if not step.executed and self in step.before:
                return False
        return True
    
    def __len__(self):
        return len(self.order)

    def __str__(self):
        return self.letter

for relationship in data.splitlines():
    step, before = map(
        lambda m: Step(m.strip()), 
        re.findall(r'[A-Z]\s', relationship)
        )
    step.before.append(before)

def find_next(steps):
    ready = filter(lambda s: s.ready, steps)
    return sorted(ready, key=str)[0]

@timed
def part_one(steps):
    order = ''
    while steps:
        next = find_next(steps)
        order += str(next)
        next.executed = True
        steps.remove(next)
    return order

steps = list(Step.cache.values())

print(part_one(steps))
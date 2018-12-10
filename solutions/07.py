from dataclasses import dataclass, field
from string import ascii_uppercase

import re

from aocd import data
from utils import timed, memoized

@memoized
@dataclass
class Step:
    letter: str
    completed: bool = False
    before: set = field(default_factory=set)

    @property # added for part 2
    def execution_time(self):
        return ascii_uppercase.index(self.letter) + 1 + 60

    @property
    def ready(self):
        all_steps = self.cache.values()
        for step in all_steps:
            if not step.completed and self in step.before:
                return False
        return True
    
    def __repr__(self):
        return self.letter
    
    def __hash__(self):
        return hash(self.letter)

def next_ready(steps):
    """Finds the next ready step from a list of steps"""
    ready = filter(lambda s: s.ready, steps)
    ret = sorted(ready, key=str) # sort alphabetically
    if ret:
        steps.remove(ret[0])
        return ret[0]

@timed
def part_one(steps):
    order = ''
    while steps:
        next = next_ready(steps)
        order += str(next)
        next.completed = True
    return order

# Added code below for part 2

@dataclass
class Worker:
    id: int
    job: Step = None
    elapsed: int = 0

    def reset(self):
        self.job.completed = True
        self.job = None
        self.elapsed = 0

    def work(self):
        self.elapsed += 1
        if self.elapsed == self.job.execution_time:
            ret = self.elapsed
            self.reset()

@timed
def part_two(all_steps, workers=5):
    time = 0
    jobs = all_steps.copy()
    workers = [Worker(i+1) for i in range(workers)]

    while not all(j.completed for j in jobs):
        time += 1
        for elf in workers:
            elf.job = elf.job or next_ready(all_steps)
        [elf.work() for elf in workers if elf.job]
        
    return time


# Processing input 

all_steps = set()

for relationship in data.splitlines():
    step, before = map(
        lambda m: Step(m.strip()), 
        re.findall(r'[A-Z]\s', relationship)
        )
    all_steps.update({step, before})
    step.before.add(before)


# print(part_one(all_steps))
print(part_two(all_steps))
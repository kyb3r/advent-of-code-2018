from dataclasses import dataclass, field

@dataclass
class Scoreboard:
    scores: list = None
    elfs: list = None

    def extend(self):
        new = str(sum(e.recipe for e in elfs))
        self.scores += [int(i) for i in new]
        for elf in self.elfs:
            next(elf)

@dataclass
class Elf:
    index: int
    scoreboard = Scoreboard([3, 7])

    @property
    def recipe(self):
        return self.scoreboard.scores[self.index]
    
    def __next__(self):
        self.index = (self.index + self.recipe + 1) % len(self.scoreboard.scores)

scoreboard = Elf.scoreboard
elfs = [Elf(0), Elf(1)]
scoreboard.elfs = elfs

def part_one(after):
    while len(scoreboard.scores) < 10 + after:
        scoreboard.extend()
    return ''.join(str(x) for x in scoreboard.scores[after:])

def part_two(sequence):
    length = len(sequence)
    index = 0
    while True:
        part = ''.join(str(c) for c in scoreboard.scores[index:index+length])
        if part == sequence:
            return len(scoreboard.scores[:index])
        scoreboard.extend()
        index += 1

print(part_one(503761))
print(part_two('59414'))
from aocd import data
from collections import deque, defaultdict
from utils import timed
import re 

players, last_marble = map(int, re.findall(r'\d+', data))

@timed
def play(players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print(play(players, last_marble)) # part 1
print(play(players, last_marble*100)) # part 2
from utils import memoized, timed

def cell_power_level(x, y, serial=5093):
    return ((x + 10) * y + serial) * (x + 10) % 1000 // 100 - 5

def square_power_level(coords, size=3):
    x, y = coords
    ret = sum(
        cell_power_level(nx, ny) 
        for nx in range(x, x+size) 
        for ny in range(y, y+size)
        )
    return ret

@timed
def max_square_power_level(size=3):
    limit = range(1, 301-size)
    return max(
        ((x, y) for x in limit for y in limit), 
        key=lambda c:square_power_level(c, size)
        )

def part_one():
    return max_square_power_level(size=3)

def part_two():
    max = ((0, 0), 0, 0)
    for size in range(1, 300):
        coords = max_square_power_level(size)
        power = square_power_level(coords)
        compare = (coords, power, size)
        max = compare if power > max[1] else max
    return max

print(part_one())
print(part_two()) # takes forever, use a summed area table instead.
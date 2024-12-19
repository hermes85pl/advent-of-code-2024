import sys

from common import blinknlen

stones = [int(x) for x in sys.stdin.read().split()]

total = sum(blinknlen(stone, 25) for stone in stones)

assert total == 190865

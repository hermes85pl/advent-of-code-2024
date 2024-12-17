import sys

from common import setup

blinknlen = setup()

stones = [int(x) for x in sys.stdin.read().split()]

total = sum(blinknlen(stone, 75) for stone in stones)

assert total == 225404711855335

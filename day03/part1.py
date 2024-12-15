import re
import sys

PATTERN = re.compile(r"mul\((\d+),(\d+)\)")

total = sum(int(a) * int(b) for a, b in PATTERN.findall(sys.stdin.read()))

assert total == 182780583

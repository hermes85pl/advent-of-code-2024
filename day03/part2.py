import re
import sys

PATTERN = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")

enabled = True
total = 0

for match in PATTERN.finditer(sys.stdin.read()):
    if match[0] == "do()":
        enabled = True
    elif match[0] == "don't()":
        enabled = False
    elif enabled:
        total += int(match[1]) * int(match[2])

assert total == 90772405

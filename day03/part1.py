import re
import sys

p = re.compile(r"mul\((\d+),(\d+)\)")

total = sum(int(a) * int(b) for a, b in p.findall(sys.stdin.read()))

assert total == 182780583

import sys
from itertools import takewhile

from common import execute

registries = [
    int(line.rstrip().rpartition(" ")[2])
    for line in takewhile(lambda l: l != "\n", sys.stdin)
]

program = [int(x) for x in sys.stdin.readline().rstrip().partition(" ")[2].split(",")]

output_str = ",".join(str(x) for x in execute(program, registries))

assert output_str == "7,5,4,3,4,5,3,4,6"

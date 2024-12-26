import sys
from itertools import takewhile

Schema = tuple[int, ...]

FILL_CHAR = "#"
SCHEMA_LEN = 5
MAX_FILL = 5

keys: list[Schema] = []
locks: list[Schema] = []

while diagram := list(takewhile(lambda l: l != "\n", sys.stdin)):
    lock = diagram[0][0] == FILL_CHAR
    m = diagram[1:-1]
    rows = m if lock else m[::-1]
    schema: Schema = tuple(
        sum(1 for _ in takewhile(lambda r: r[i] == FILL_CHAR, rows))
        for i in range(SCHEMA_LEN)
    )
    (locks if lock else keys).append(schema)

total = sum(
    all(k + l <= MAX_FILL for k, l in zip(key, lock)) for key in keys for lock in locks
)

assert total == 3671

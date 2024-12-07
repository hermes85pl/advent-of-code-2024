import sys


def calc(vals: list[int], res: int, acc: int = 0) -> bool:
    if len(vals) == 0:
        return res == acc
    return acc <= res and (
        calc(vals[1:], res, acc + vals[0]) or calc(vals[1:], res, acc * vals[0])
    )


total = 0

for line in sys.stdin:
    res_str, vals_str = line.rstrip().partition(": ")[::2]
    res = int(res_str)
    total += res if calc([int(x) for x in vals_str.split()], res) else 0

assert total == 5512534574980

import sys


def calc(res: int, vals: list[int], acc: int = 0) -> bool:
    if not vals:
        return res == acc
    if acc > res:
        return False
    head, rest = vals[0], vals[1:]
    return (
        calc(res, rest, acc + head)
        or calc(res, rest, acc * head)
        or calc(res, rest, int(f"{acc}{head}"))
    )


total = 0

for line in sys.stdin:
    res_str, vals_str = line.rstrip().partition(": ")[::2]
    res = int(res_str)
    total += res if calc(res, [int(x) for x in vals_str.split()]) else 0

assert total == 328790210468594

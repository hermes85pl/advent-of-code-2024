r1, r2 = set(), {}

with open("input.txt") as f:
    while l := f.readline().strip():
        a, b = [int(x) for x in l.split()]
        r1.add(a)
        r2[b] = r2.get(b, 0) + 1

total = sum(x * r2.get(x, 0) for x in r1)

assert total == 24643097

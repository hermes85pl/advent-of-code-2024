from common import machines, solve

total = sum(solve(*machine) for machine in machines())

assert total == 31623

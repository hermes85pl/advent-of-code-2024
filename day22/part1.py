import sys

from common import evolve

secrets = [int(line.rstrip()) for line in sys.stdin]

for _ in range(2000):
    secrets = [evolve(secret) for secret in secrets]

total = sum(secrets)

assert total == 15303617151

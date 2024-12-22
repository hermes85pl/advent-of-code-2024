import sys
from collections import Counter, deque

from common import evolve

Sequence = tuple[int, ...]

secrets = [int(line.rstrip()) for line in sys.stdin]

total_scores: Counter[Sequence] = Counter()
for secret in secrets:
    window: deque[int] = deque(maxlen=4)
    scores: dict[Sequence, int] = {}
    last_value = 0
    for _ in range(2000):
        secret = evolve(secret)
        value = secret % 10
        window.append(value - last_value)
        if len(window) == 4 and (sequence := tuple(window)) not in scores:
            scores[sequence] = value
        last_value = value
    total_scores += scores

result = total_scores.most_common(1)[0][1]

assert result == 1727

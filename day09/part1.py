import sys
from collections import deque


def segment(i: int, c: int) -> tuple[int, int]:
    return (i // 2 if i % 2 == 0 else -1, c)


def compacted_blocks(segments: deque[tuple[int, int]]):
    while segments:
        segment_id, segment_len = segments.popleft()
        if segment_id >= 0:
            yield from (segment_id for _ in range(segment_len))
            continue
        while segments and segment_len > 0:
            new_segment_id, new_segment_len = segments.pop()
            if new_segment_id < 0:
                continue
            if new_segment_len <= segment_len:
                yield from (new_segment_id for _ in range(new_segment_len))
                segment_len -= new_segment_len
            else:
                yield from (new_segment_id for _ in range(segment_len))
                segments.append((new_segment_id, new_segment_len - segment_len))
                segment_len = 0


segments = deque(segment(i, int(c)) for i, c in enumerate(sys.stdin.read().rstrip()))

total = sum(i * v for i, v in enumerate(compacted_blocks(segments)))

assert total == 6366665108136

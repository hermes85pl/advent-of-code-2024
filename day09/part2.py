import sys
from collections import deque
from typing import Iterable


def segment(i: int, c: int) -> tuple[int, int]:
    return (i // 2 if i % 2 == 0 else -1, c)


def compact(segments: deque[tuple[int, int]]) -> None:
    right_segment_stack: list[tuple[int, int]] = []
    while segments:
        right_segment_id, right_segment_len = segments.pop()
        if right_segment_id < 0:
            right_segment_stack.append((right_segment_id, right_segment_len))
            continue
        left_segment_stack: list[tuple[int, int]] = []
        while segments:
            left_segment_id, left_segment_len = segments.popleft()
            if left_segment_id >= 0 or left_segment_len < right_segment_len:
                left_segment_stack.append((left_segment_id, left_segment_len))
                continue
            segment_len_diff = left_segment_len - right_segment_len
            if segment_len_diff > 0:
                segments.appendleft((-1, segment_len_diff))
            segments.appendleft((right_segment_id, right_segment_len))
            right_segment_stack.append((-1, right_segment_len))
            break
        else:
            right_segment_stack.append((right_segment_id, right_segment_len))
        segments.extendleft(reversed(left_segment_stack))
    segments.extend(reversed(right_segment_stack))


def blocks(segments: Iterable[tuple[int, int]]):
    for segment_id, segment_len in segments:
        yield from (segment_id for _ in range(segment_len))


segments = deque(segment(i, int(c)) for i, c in enumerate(sys.stdin.read().rstrip()))

compact(segments)

total = sum(i * v for i, v in enumerate(blocks(segments)) if v >= 0)

assert total == 6398065450842

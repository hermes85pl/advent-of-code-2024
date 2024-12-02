def safe(levels: list[int]) -> bool:
    prev_diff = 0
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if diff == 0 or abs(diff) > 3 or diff * prev_diff < 0:
            return False
        prev_diff = diff
    return True

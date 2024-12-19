from common import load

patterns, designs = load()


def check_possible(design) -> bool:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        if dp[i]:
            for j in range(i + 1, len(dp)):
                if design[i:j] in patterns:
                    dp[j] = True
    return dp[n]


total = sum(check_possible(design) for design in designs)

assert total == 350

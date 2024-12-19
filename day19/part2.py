from common import load

patterns, designs = load()


def count_ways(design) -> int:
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if dp[i]:
            for j in range(i + 1, len(dp)):
                if design[i:j] in patterns:
                    dp[j] += dp[i]
    return dp[n]


total = sum(count_ways(design) for design in designs)

assert total == 769668867512623

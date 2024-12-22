MODULUS = 16777216


def evolve(secret: int) -> int:
    secret ^= secret * 64
    secret %= MODULUS
    secret ^= secret // 32
    secret %= MODULUS
    secret ^= secret * 2048
    secret %= MODULUS
    return secret

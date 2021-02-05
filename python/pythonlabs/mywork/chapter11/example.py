off_cache = {}

def offset(n: int) -> int:
    if n < 0: return 0
    elif n == 1: return 1
    elif n in off_cache: return off_cache[n]
    k = lambda n: (n >> 1) * (1 - (n & 1)) + n * (n & 1)
    r = sum(k(i) for i in range(n, 0, -1))
    off_cache[n] = r
    return r

p_cache = {}

def p(n: int) -> int:
    if n < 0: return 0
    elif n <= 1: return 1
    elif n in p_cache: return p_cache[n]
    s = 0
    o = offset(1)
    i = 0
    while o <= n:
        s += p(n - o) * (((i >> 1) % 2) * -2 + 1)
        i += 1
        o = offset(i + 1)
    p_cache[n] = s
    return s

print('p(666)', p(666))
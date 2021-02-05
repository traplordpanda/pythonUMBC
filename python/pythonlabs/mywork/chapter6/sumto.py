def sumUpTo(n):
    if not n:
        return n
    return n + sumUpTo(n-1)


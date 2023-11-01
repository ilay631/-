from functools import lru_cache


@lru_cache(None)
def f(a, b, c):
    if a == b:
        if "CAC" in c:
            return 1
        else:
            return 0
    if a > b:
        return 0
    if a < b:
        return f(a + 1, b, c + 'A') + f(a * 3, b, c + 'B') + f(a + 5, b, c + 'C')


print(f(3, 69, ""))

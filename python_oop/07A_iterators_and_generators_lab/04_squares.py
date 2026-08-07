from collections.abc import Generator


def squares(n: int) -> Generator[int, None, None]:
    for number in range(1, n + 1):
        yield number ** 2
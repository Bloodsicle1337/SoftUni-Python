from collections.abc import Generator, Iterable


def solution():
    def integers() -> Generator[int, None, None]:
        number = 1

        while True:
            yield number
            number += 1

    def halves() -> Generator[float, None, None]:
        for number in integers():
            yield number / 2

    def take(n: int, seq: Iterable[float]) -> list[float]:
        result = []

        for _ in range(n):
            result.append(next(seq))

        return result

    return take, halves, integers
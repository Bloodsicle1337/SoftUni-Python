from collections.abc import Generator, Iterable
from typing import Any


def read_next(*args: Iterable[Any]) -> Generator[Any, None, None]:
    for iterable in args:
        for element in iterable:
            yield element
from collections.abc import Generator
from typing import Any


def possible_permutations(
    elements: list[Any]
) -> Generator[list[Any], None, None]:
    if len(elements) == 1:
        yield elements
        return

    for index in range(len(elements)):
        current_element = elements[index]
        remaining_elements = elements[:index] + elements[index + 1:]

        for permutation in possible_permutations(remaining_elements):
            yield [current_element] + permutation